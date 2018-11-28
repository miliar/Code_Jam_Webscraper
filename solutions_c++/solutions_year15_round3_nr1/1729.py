#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
	int t,r,c,w,flag=1;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&c,&w);
		int ans=c/w;
		ans+=w-1;
		if(c%w==0)
		{
			printf("Case #%d: %d\n",flag++,ans);
			continue;
		}
		ans++;
		printf("Case #%d: %d\n",flag++,ans);
	}
	return 0;
}
