#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;

template <class T>
void read(T &x)
{
	char ch;
	for (ch=getchar();(ch<'0'||ch>'9')&&ch!='-';) ch=getchar();
	x=0;int t=1;if (ch=='-') {ch=getchar();t=-1;}
	for (;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-'0';
	x*=t;
}

double a[210],b[210],dp[210][210];

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		int n,k;read(n);read(k);
		for (int i=1;i<=n;i++) scanf("%lf",&a[i]);
		sort(a+1,a+n+1);for (int i=1;i<=n;i++) a[n+i]=a[i];
		double ans=0;
		for (int p=1;p<=n;p++)
		{
			for (int j=1;j<=k;j++) b[j]=a[p+j-1];
			memset(dp,0,sizeof(dp));dp[0][0]=1;
			for (int i=1;i<=k;i++)
			{
				for (int j=i;j>=1;j--)
					dp[i][j]=dp[i-1][j]*b[i]+dp[i-1][j-1]*(1-b[i]);
				dp[i][0]=dp[i-1][0]*b[i];
			}
			ans=max(ans,dp[k][k/2]);
		}
		printf("Case #%d: %.10lf\n",T,ans);
	}
	return 0;
}

