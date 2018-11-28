#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
using namespace std;    
const int N = 205, mod = int(1e9)  + 7;
int T;
long double dp[N][N];
int n,k,cn;
double p[N],c[N];

int main () {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%lf",&p[i]);
		}
		ld ans = 0;
		for(int mask=0;mask<(1<<n);mask++) if(__builtin_popcount(mask) == k){
			cn = 0;
			for(int i=0;i<n;i++){
				if((mask & (1<<i))){
					c[++cn] = p[i];
				}
			}
			dp[1][1] = c[1];
			dp[1][0]  = 1 - c[1];
			for(int i=2;i<=cn;i++){
				dp[i][0] = dp[i-1][0] * (1 - c[i]);
				for(int j=1;j<=k/2;j++){
					dp[i][j] = dp[i-1][j-1] * c[i] + dp[i-1][j] * (1 - c[i]);
				}	
			}
			ans = max(ans,dp[k][k/2]);
		}
		printf("%.12lf\n",(double)ans);
	}

return 0;
}