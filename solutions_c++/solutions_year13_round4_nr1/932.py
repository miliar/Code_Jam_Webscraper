#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<map>
#include<vector>

#define pb push_back
#define mp make_pair

typedef long long big;
using namespace std;
const int N=2020;
int n,m;
big P=1000002013;
big a[N],b[N],c[N];
big f[N];
big g[N];
int main()
{
	int cas,cass,i,j;
	map<int,int>::iterator it;
	big u;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	big ans=0,t,man,former,now;
	scanf("%d",&cas);
	big k;
	for(cass=1;cass<=cas;cass++)
	{
		ans=0;t=0;man=0;
		scanf("%d%d",&n,&m);
		former=0;
		memset(f,0,sizeof(f));
		memset(g,0,sizeof(g));
		for(i=1;i<=m;i++)
		{
			scanf("%I64d%I64d%I64d",&a[i],&b[i],&c[i]);
			f[a[i]]+=c[i];
			f[b[i]]-=c[i];
			k=b[i]-a[i];
			former+=1ll*(2ll*n-k+1)*k/2%P*c[i]%P;
			former%=P;
		}
		for(i=1;i<=n;i++)
		{
			ans+=t;
			if(f[i]>0)
			{
				g[i]+=f[i];
				man+=f[i];
				t+=f[i]*(n+1);
			}
			else if(f[i]<0)
			{
				now=-f[i];
				for(j=i-1;j>=1;j--)
					if(g[j]>0)
					{
						u=min(g[j],now);
						g[j]-=u;
						man-=u;
						now-=u;
						t-=u*(n-i+j+1);
					}
			}
			t-=man;
			//printf("%I64d %I64d %I64d\n",ans,t,f[i]);
		}
		ans%=P;
		if(ans<0)ans+=P;
		ans=(former-ans)%P;
		if(ans<0)ans+=P;
		printf("Case #%d: %I64d\n",cass,ans);
	}
}
