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
#define EPS 1e-13


typedef long double D;

void prepare(){
	
}


D solve(){
	int n;
	D V, X;
	cin >> n >> V >> X;
	D ret = -1;
	if(n == 1){
		D r, c;
		cin >> r >> c;
		if(c == X){
			ret = V / r;
		}
	}
	else if(n == 2){
		D r1, c1, r2, c2;
		cin >> r1 >> c1 >> r2 >> c2;
		if(r1 > r2){
			swap(r1, r2);
			swap(c1, c2);
		}
		
		if(c1 == X && c2 == X){
			ret = V / (r1 + r2);
		}
		else if(c2 == X){
			ret = V / r2;
		}
		else if(c1 == X){
			ret = V / r1;
		}
		else{
			D y1 = r1 * c1, y2 = r2 * c2;
			D W = V * X;
			if(r1 * y2 != r2 * y1){
				D d = 1 / (r1 * y2 - r2 * y1);
				D s1 = (V * y2 - r2 * W) * d;
				D s2 = (r1 * W - V * y1) * d;
				if(s1 > -EPS && s2 > -EPS){
					ret = max({s1, s2, D()});
				}
			}
		}
	}
	return ret;
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
		if(ans < 0){ cout << "IMPOSSIBLE" << endl; }
		else{ cout << ans << endl; }
	}
}
