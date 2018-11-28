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


LL solve(){
	int p, q, n;
	cin >> p >> q >> n;
	vector<int> hs(n), gs(n), ss(n), ts(n);
	for(int i = 0; i < n; ++i){
		cin >> hs[i] >> gs[i];
		ts[i] = (hs[i] - 1) / q;
		ss[i] = (hs[i] - ts[i] * q + p - 1) / p;
	}
	
	const int INF = 1010101010;
	vector<int> dp1(1500, -INF), dp2(1500, -INF);
	dp1[1] = 0;
	for(int i = 0; i < n; ++i){
		for(int j = 0; j < 1400; ++j){
			int &x = dp2[j + ts[i] + 1];
			x = max(x, dp1[j]);
			if(j >= ss[i] - ts[i]){
				int &y = dp2[j - ss[i] + ts[i]];
				y = max(y, dp1[j] + gs[i]);
			}
		}
		dp1.swap(dp2);
		fill(ALL(dp2), -INF);
	}
	
	int res = *max_element(ALL(dp1));

	return res;
}


int main(){
	cout << fixed << setprecision(15);
	cerr << fixed << setprecision(6);

	int T = 0;
	cin >> T;
	for(int cnum = 1; cnum <= T; ++cnum){
		fprintf(stderr, "%4d / %d\n", cnum, T);
		cout << "Case #" << cnum << ": " << flush;
		auto ans = solve();
		cout << ans << endl;
	}
}
