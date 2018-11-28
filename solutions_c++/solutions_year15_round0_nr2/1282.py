#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#define _USE_MATH_DEFINES
#include <cmath>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <cassert>
using namespace std;

#define EPS 1e-12
#define ull unsigned long long
#define ll long long
#define VI vector<ll>
#define PII pair<ll, ll> 
#define VVI vector<vector<ll> >
#define REP(i,n) for(int i=0,_n=(n);(i)<(int)_n;++i)
#define RANGE(i,a,b) for(int i=(int)a,_b=(int)(b);(i)<_b;++i)
#define RANGE_R(i,a,b) for(int i=(int)b-1,_a=(int)(a);(i)>=_a;--i)
#define MIN_UPDATE(target, value) target = min(target, value)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define ALLR(c) (c).rbegin(), (c).rend()
#define PB push_back
#define MP(a, b) make_pair(a, b)
#define POPCOUNT __builtin_popcount
#define POPCOUNTLL __builtin_popcountll
#define CLEAR(table, v) memset(table, v, sizeof(table));
#define PRINT1(table, D0) REP(d0, D0) cout<<table[d0]<<" "; cout<<"\n";
#define PRINT2(table, D0, D1) REP(d0, D0) { REP(d1, D1) cout<<table[d0][d1]<<" "; cout<<"\n"; }
#define PRINT3(table, D0, D1, D2) REP(d0, D0) { REP(d1, D1) { REP(d2, D2) cout<<table[d0][d1][d2]<<" "; cout<<"\n"; } cout<<"\n"; }
template <typename T0, typename T1> std::ostream& operator<<(std::ostream& os, const map<T0, T1>& v) { for( typename map<T0, T1>::const_iterator p = v.begin(); p!=v.end(); p++ ){os << p->first << ": " << p->second << " ";} return os; }
template <typename T0, typename T1> std::ostream& operator<<(std::ostream& os, const pair<T0, T1>& v) { os << v.first << ": " << v.second << " "; return os; }
template <typename T> std::ostream& operator<<(std::ostream& os, const vector<T>& v) { for( int i = 0; i < (int)v.size(); i++ ) { os << v[i] << " "; } return os; }
template <typename T> std::ostream& operator<<(std::ostream& os, const set<T>& v) { vector<T> tmp(v.begin(), v.end()); os << tmp; return os; }
template <typename T> std::ostream& operator<<(std::ostream& os, const deque<T>& v) { vector<T> tmp(v.begin(), v.end()); os << tmp; return os; }
template <typename T> std::ostream& operator<<(std::ostream& os, const vector<vector<T> >& v) { for( int i = 0; i < (int)v.size(); i++ ) { os << v[i] << endl; } return os; }


ll naive(ll N, VI PP) {
	ll maxP = *max_element(ALL(PP));
	ll ans = 100000;
	REP(b, 1<<(maxP+1)) {
		ll lans = 0;
		VI P(PP);
		REP(i, maxP+1) {
			lans++;
			if((b>>i)&1) {
				//sp
				ll mi = distance(P.begin(), max_element(ALL(P)));
//				cout<<P<<" "<<mi<<endl;
				ll take = P[mi]/2;
				P[mi]-=take;
				P.PB(take);
			} else {
				REP(j, P.size()) if(P[j]) P[j]--;
			}
			if(*max_element(ALL(P))==0) break;
		}
		ans = min(ans, lans);
	}
	return ans;
}

/*

*/
int main() {
	int test_cases;
	cin>>test_cases;
	ll N;
	string s;
	REP(ttt, test_cases) {
		cin>>N;
		VI P(N);
		REP(i, N) cin>>P[i];
		ll maxP = *max_element(ALL(P));
		ll ans = 100000;
		RANGE(ms, 1, maxP+1) {
			ll lans = 0;
			REP(i, N) lans+=(P[i]+ms-1)/ms-1;
			lans += ms;
//			cout<<ms<<" : "<<lans<<endl;
			ans = min(ans, lans);
		}
//		if(maxP<=15) {
//			ll nans = naive(N, P);
//			if(nans>ans) {
//				cout<<"nans bit worse but OK "<<ttt+1<<" "<<ans<<" "<<nans<<endl;
//			}
//			if(nans<ans) {
//				cout<<"!!! "<<ttt+1<<" "<<ans<<" "<<nans<<endl;
//				assert(false);
//			}
//			cout<<"Check OK for "<<ttt+1<<endl;
//		}
		cout<<"Case #"<<ttt+1<<": "<<ans<<endl;
//		return 0;
	}
	return 0;
}



