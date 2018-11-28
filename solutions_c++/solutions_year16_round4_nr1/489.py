#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <deque>
#include <complex>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <ctime>
#include <iterator>
#include <bitset>
#include <numeric>
#include <list>
#include <iomanip>
#include <cassert>

#if __cplusplus >= 201103L
#include <array>
#include <tuple>
#include <initializer_list>
#include <unordered_set>
#include <unordered_map>
#include <forward_list>

#define cauto const auto&
#endif

using namespace std;


namespace{

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;
typedef vector<long long> vll, vLL;
typedef vector<vector<long long> > vvll, vvLL;

#define VV(T) vector<vector< T > >

template <class T, class U=T>
void initvv(vector<vector<T> > &v, int a, int b, const U &t = U()){
	v.assign(a, vector<T>(b, t));
}

template <class F, class T>
void convert(const F &f, T &t){
	stringstream ss;
	ss << f;
	ss >> t;
}

template <class Con>
string concat(const Con &c, string spl){
	stringstream ss;
	typename Con::const_iterator it = c.begin(), en = c.end();
	bool fst = true;
	for(; it != en; ++it){
		if(!fst){ ss << spl; }
		fst = false;
		ss << *it;
	}
	return ss.str();
}


#define REP(i,n) for(int i=0;i<int(n);++i)
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(),(v).rend()
#define PB push_back


#define MOD 1000000009LL
#define EPS 1e-8

string tbl[13][3];

void prepare(){
//	ios::sync_with_stdio(false);
	
	tbl[0][0] = 'R';
	tbl[0][1] = 'P';
	tbl[0][2] = 'S';

	for(int n = 1; n <= 12; ++n){
		for(int i = 0; i < 3; ++i){
			string s = tbl[n - 1][i];
			string t = tbl[n - 1][(i + 1) % 3];
			if(s > t){ s.swap(t); }
			tbl[n][(i + 1) % 3] = s + t;
		}
	}
}


string solve(){
	string res = "~";
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	for(int i = 0; i < 3; ++i){
		const string &t = tbl[n][i];
		if(t < res){
			if(count(ALL(t), 'R') != r){ continue; }
			if(count(ALL(t), 'P') != p){ continue; }
			if(count(ALL(t), 'S') != s){ continue; }
			res = t;
		}
	}
	if(res == "~"){
		res = "IMPOSSIBLE";
	}
	return res;
}


}
int main(){
	cout << fixed << setprecision(15);
	cerr << fixed << setprecision(6);
	prepare();

	string str = "_";
	getline(cin, str);
	int T = strtol(str.c_str(), 0, 10);
	for(int cnum = 1; cnum <= T; ++cnum){
		fprintf(stderr, "%4d / %d\n", cnum, T);
		cout << "Case #" << cnum << ": " << flush;
		auto ans = solve();
		cout << ans << endl;
	}
}
