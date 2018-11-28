#include<stdio.h>
#include<algorithm>
using namespace std;
const int Maxn=1020;
int a[Maxn];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int _,cs=1;scanf("%d",&_);
	while(_--)
	{
		int n;scanf("%d",&n);
		for(int i=1;i<=n;i++)scanf("%d",a+i);
		int ans=1000;
		for(int h=1;h<=1000;h++)
		{
			int t=h;
			for(int i=1;i<=n;i++)
			{
				if(a[i]<=h)continue;
				t+=(a[i]-h)/h+(((a[i]-h)%h)!=0);
			}
			ans=min(ans,t);
		}
		printf("Case #%d: %d\n",cs++,ans);
	}
}
