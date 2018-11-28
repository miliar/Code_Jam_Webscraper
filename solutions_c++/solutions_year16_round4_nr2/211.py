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

long double p[207], dp[207][207], ar[207];

long double go(int n, int k){
	set0(dp);
	dp[0][0] = 1.0;
	FOR(i, 1, n+1){
		dp[i][0] = ar[i] * dp[i-1][0];
		FOR(j, 1, k+1){
			if(j > i) continue;
			dp[i][j] = (ar[i] * dp[i-1][j]) + ((1.0 - ar[i]) * dp[i-1][j-1]);
		}
	}
	return dp[n][k];
}
int main() {
	freopen("a.in", "r", stdin);
    freopen("a1.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
    FOR(ts, 1, T+1){
		int n, k; cin >> n >> k;
		REP(i, n) cin >> p[i+1];
		sort(p + 1, p + n + 1);
		long double res = 0;
		
		for(int i = 0; i <= k; i++){
			int cc = 0;
			for(int j = 1; j <= i; j++) ar[++cc] = p[j];
			for(int j = n-(k-i)+1; j <= n; j++) ar[++cc] = p[j];
		
			res = max(res, go(cc, k/2));
		}
		
        cout << "Case #" << ts << ": ";
        cout << fixed << setprecision(10) << res << endl;
	}
}
