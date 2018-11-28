#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<iostream>
#include<map>
using namespace std;
const int INF = 1000000005;
const int N = 1005;
int lf[N],rf[N],a[N],b[N],ps[N],f[N];
bool cmp(int x,int y){return a[x]<a[y];}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		int n,i,j;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			b[i]=i;
			f[i]=ps[i]=i;
		}
		sort(b+1,b+n+1,cmp);
		int ret=0,ll=1,rr=n;
		for(i=1;i<=n;i++)
		{
			int x=b[i],p=ps[x];
			int ld=p-ll,rd=rr-p;
			//printf("x:%d p:%d ld:%d rd:%d ll:%d rr:%d \n",x,p,ld,rd,ll,rr);
			if(ld<rd)
			{
				ret+=ld;
				for(j=p-1;j>=ll;j--)
				{
					f[j+1]=f[j];
					ps[f[j]]=j+1;
				}
				ll++;
			}
			else
			{
				ret+=rd;
				for(j=p+1;j<=rr;j++)
				{
					f[j-1]=f[j];
					ps[f[j]]=j-1;
				}
				rr--;
			}
		}
		printf("%d\n",ret);
	}
	return 0;
}