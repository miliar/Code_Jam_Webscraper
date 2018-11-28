#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[1024],l,r,n,Testcase;
bool check(int mid)
{

	for(int eattime=1;eattime<=mid;++eattime)
	{
		int movetime=mid-eattime;
		int flag=1;
		for(int i=1;i<=n;i++)
			if(a[i]>eattime)
			{
				movetime-=(a[i]-1)/eattime;
				if(movetime<0)break;
			}
		if(movetime>=0)return 1;
	}
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&Testcase);
	for(int t=1;t<=Testcase;++t)
	{
		scanf("%d",&n);
		r=0;
		for(int i=1;i<=n;++i)
		{
			scanf("%d",&a[i]);
			r=max(r,a[i]);
		}
		
		l=1;r+=10;
		while(l<r)
		{
			int mid=(l+r)>>1;
			if(check(mid))r=mid;
			else l=mid+1;
		}
		printf("Case #%d: %d\n",t,r);
	}
}