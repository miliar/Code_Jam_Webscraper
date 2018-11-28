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
	int n;
	char c;
	cin >> n;
	vector<int> as(n), ids(n);
	vector<int> setids(1);
	for(int i = 0; i < n; ++i){
		cin >> c >> ids[i];
		as[i] = (c == 'E');
		setids.push_back(ids[i]);
	}
	sort(ALL(setids));
	setids.erase(unique(ALL(setids)), setids.end());
	for(int i = 0; i < n; ++i){
		ids[i] = lower_bound(ALL(setids), ids[i]) - setids.begin();
	}

	int m = setids.size() - 1;
	int b = m + 4;
	int last = 1 << b;
	vector<char> dp1(last, 1), dp2(last);
	for(int i = 0; i < n; ++i){
		int id = ids[i];
		if(id == 0){
			for(int S = last; S--; ){
				if(!dp1[S]){ continue; }
				for(int k = 0; k < m; ++k){
					if((S >> k & 1) != as[i]){
						dp2[S ^ (1 << k)] = 1;
					}
				}
				
				if(as[i]){
					if((S >> m) != 15){
						dp2[S + (1 << m)] = 1;
					}
				}
				else if(S >> m){
					dp2[S - (1 << m)] = 1;
				}
			}
		}
		else{
			for(int S = last; S--; ){
				if(!dp1[S]){ continue; }
				if((S >> (id - 1) & 1) != as[i]){
					dp2[S ^ (1 << (id - 1))] = 1;
				}
			}
		}
		
		dp1.swap(dp2);
		dp2.assign(last, 0);
	}

	int res = 1010101010;
	for(int S = last; S--; ){
		if(dp1[S]){
			int cnt = __builtin_popcount(S & ((1 << m) - 1)) + (S >> m);
			res = min(res, cnt);
		}
	}
	
	if(res > 10000){
		res = -1;
	}

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
		if(ans < 0){
			cout << "CRIME TIME\n";
		}
		else{
			cout << ans << endl;
		}
	}
}
