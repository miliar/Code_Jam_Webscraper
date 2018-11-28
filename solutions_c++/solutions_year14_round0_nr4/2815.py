#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

#define N 600
#define inf 0x3f3f3f3f
#define eps 1e-8
#define ll long long

ll mm=1000000007;
ll s1,s23,s3,ans;
double a[1001],b[1001];
bool v[1001];
int main()
{
	freopen("a.out","w",stdout);
	freopen("D-large.in","r",stdin);
	int T,cas=0,n;
	cin>>T;
	while (T--)
	{
		cin>>n;
		for (int i=1;i<=n;i++)
			scanf("%lf",&a[i]);
		sort(a+1,a+n+1);
		for (int i=1;i<=n;i++)
			scanf("%lf",&b[i]);
		sort(b+1,b+n+1);
		int ans1=0;
		for (int i=1;i<=n;i++)
		{
			int p=i-1;
			int o=0;
			for (int j=1;j<=n;j++)
			{
				p++;if (p>n) break;
				if (a[p]<b[j]) {o=1;break;}
			}
//			cout<<o<<endl;
			if (!o){
				ans1=n+1-i;
				break;
			}
		}
		int ans2=n;
		memset(v,0,sizeof(v));
		for (int i=1;i<=n;i++)
		{
			int ok=0;
			for (int j=1;j<=n;j++)
				if (b[j]>a[i]&&!v[j])
				{
					v[j]=1;
					ans2--;
					ok=1;
					break;
				}
			if (!ok)
				for (int j=1;j<=n;j++)
					if (!v[j])
					{
						v[j]=1;
						break;
					}
		}
		printf("Case #%d: ",++cas);
		cout<<ans1<<' '<<ans2<<endl;
	}
}