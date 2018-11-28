#include <stdio.h>

int main(void) {
	// your code goes here
	freopen("gcjl15.in","r",stdin);
	freopen("outputgcja.txt","w",stdout);
	int t,n,a[1005],i,j,cnt,sum[1005];
	char s[1005];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{

		scanf("%d",&n);
		scanf("%s",s);
		for(j=0;j<=n;j++)
		{
			a[j]=s[j]-'0';
		}
		cnt=0;
		sum[0]=0;
		for(j=1;j<=n;j++)
		sum[j]=sum[j-1]+a[j-1];
		for(j=0;j<=n;j++)
		//printf("%d %d\n",sum[j],a[j]);
		for(j=1;j<=n;j++)
		{
			if(sum[j]+cnt>=j||a[j]==0)
			continue;
			else
			{
				cnt=j-sum[j];
			}
			//printf("%d\n",cnt);
		}
		printf("Case #%d: %d\n",i,cnt);
	}
	return 0;
}

