#include <stdio.h>

using namespace std;

int main()
{
	int cnt,n,k,q,ans,num,i;
	// freopen("test.in","r",stdin);
	// freopen("test.out","w",stdout);
	scanf("%d",&q);
	for(k=1;k<=q;k++)
	{
		cnt=ans=0;
		printf("Case #%d: ",k);
		scanf("%d ",&n);
		for(i=0;i<=n;i++)
		{
			scanf("%1d",&num);
			// printf("%d %d\n",i,cnt);
			if(cnt>=i)
				cnt+=num;
			else
			{
				ans+=i-cnt;
				// printf("%d %d\n",i,cnt);
				cnt=i;
				cnt+=num;
				// printf("%d %d\n",i,cnt);
			}
			// printf("%d\n",ans);
		}
		printf("%d\n",ans);
	}
	return 0;
}