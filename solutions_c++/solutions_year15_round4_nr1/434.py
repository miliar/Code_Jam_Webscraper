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

template <class T>
void initvv(vector<vector<T> > &v, int a, int b, const T &t = T()){
	v.assign(a, vector<T>(b, t));
}

template <class F, class T>
void convert(const F &f, T &t){
	stringstream ss;
	ss << f;
	ss >> t;
}


#define REP(i,n) for(int i=0;i<int(n);++i)
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(),(v).rend()
#define PB push_back


#define MOD 1000000009LL
#define EPS 1e-8


void prepare(){
	
}

char s[128][128];
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, -1, 0, 1};

int check(int y0, int x0){
	int r = 0;
	for(int i = 0; i < 4; ++i){
		int y = y0, x = x0;
		while(1){
			y += dy[i];
			x += dx[i];
			if(!s[y][x]){ break; }
			if(s[y][x] != '.'){
				r |= 1 << i;
				break;
			}
		}
	}
	return r;
}

string solve(){
	int h, w;
	cin >> h >> w;
	
	memset(s, 0, sizeof s);
	for(int i = 1; i <= h; ++i){
		cin >> (s[i] + 1);
	}
	
	int ret = 0;
	for(int y = 1; y <= h; ++y)
	for(int x = 1; x <= w; ++x){
		if(s[y][x] == '.'){ continue; }
		int dir;
		if(s[y][x] == '^'){ dir = 0; }
		else if(s[y][x] == '<'){ dir = 1; }
		else if(s[y][x] == 'v'){ dir = 2; }
		else{ dir = 3; }

		int r = check(y, x);
		if(!r){ return "IMPOSSIBLE"; }
		if(!(r >> dir & 1)){
			++ret;
		}
	}

	string z;
	convert(ret, z);
	return z;
}


}
int main(){
	cout << fixed << setprecision(15);
	cerr << fixed << setprecision(6);
	prepare();

	int T = 0;
	cin >> T;
	for(int cnum = 1; cnum <= T; ++cnum){
		fprintf(stderr, "%4d / %d\n", cnum, T);
		cout << "Case #" << cnum << ": " << flush;
		auto ans = solve();
		cout << ans << endl;
	}
}
