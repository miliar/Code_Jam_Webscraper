#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<ctime>
#include<climits>
#include<complex>
#include<cassert>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) (int)((x).size())
#define all(x) x.begin(),x.end()
#define clr(x) memset((x),0,sizeof(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define rep(i,n) for (i=0;i<n;i++)
#define Rep(i,a,b) for (i=a;i<=b;i++)
#define ff(i,x) for (i=start[x];i!=-1;i=a[i].next)
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
const double eps=1e-8;
const double pi=acos(-1.0);
int dblcmp(double d){if (fabs(d)<eps)return 0;return d>eps?1:-1;}
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
double a[1111],b[1111];
int dp[1111][1111];
int n;
int main()
{
	int i,j,k,cas,cc=0;
	freopen("C:\\competition\\gcj\\D-large.in","r",stdin);
	freopen("C:\\competition\\gcj\\D.out","w",stdout);
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)scanf("%lf",&a[i]);
		for (i=0;i<n;i++)scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		j=-1;
		int ans=n;
		for (i=0;i<n;i++)
		{
			for (j++;j<n;j++)
			{
				if (b[j]>a[i])
				{
					ans--;
					break;
				}
			}
		}
		clr(dp);
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=n;j++)
			{
				if (a[i-1]>b[j-1])
				{
					dp[i][j]=dp[i-1][j-1]+1;
				}
				else 
				{
					dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
				}
			}
		}
		printf("Case #%d: %d %d\n",++cc,dp[n][n],ans);
	}
	return 0;
}
/*
*****
*****
**.c*
*****
*****
*/
	