#include<cstdio>
#include<cstring>
#include<cassert>
#include<vector>
#include<list>
#include<queue>
#include<map>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<fstream>
#include<typeinfo>
#include<locale>
#include<iterator>
#include<valarray>
#include<complex>
#include<climits>

using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

string ss[5];
int ar[5][5], t1[5];
int dp[1<<5][5];

int go(int bp, int c, int n){
	if(c == n) return 0;
	int &ret = dp[bp][c];
	if(ret != -1) return ret;
	ret = 0;
	int fl = 0;
	REP(i, n){
		if(ar[ t1[c] ][i] == 0 || (bp & 1<<i) > 0) continue;
		fl = 1;
		ret |= go(bp | (1<<i), c + 1, n);
	}
	
	if(fl == 0) ret = 1;
	return ret;
}

int main() {
	freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
    FOR(ts, 1, T+1){
		int n; cin >> n;
		REP(i, n) cin >> ss[i];
		
		int res = n*n;
		REP(i, 1<<(n*n)){
			set0(ar);
			REP(j, n){
				REP(k, n){
					if(ss[j][k] == '1' || (i & 1<<((j*n) + k)) > 0) ar[j][k] = 1;
				}
			}
			REP(j, n) t1[j] = j;
			int fl = 0;
			do{
				memset(dp, -1, sizeof dp);
				if(go(0, 0, n)) fl = 1;
				if(fl) break;
				
			} while(next_permutation(t1, t1 + n));
			if(fl == 0) res = min(res, __builtin_popcount(i));
			//if(fl == 0){
				//cout << i << endl;
				//REP(j, n){ 
					//REP(k, n) cout << ar[j][k] << " ";
					//cout << endl;
				//}
			//}
		}


        cout << "Case #" << ts << ": " << res << endl;
	}
}
