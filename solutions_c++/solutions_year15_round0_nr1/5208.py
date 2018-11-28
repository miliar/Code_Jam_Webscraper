#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
int main()
{
	char s[1005];
	int i,t,ans,n,cnt,k,x;
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	while(scanf("%d",&t)!=EOF)
	{
		for(k=1;k<=t;k++)
		{
			ans=0;
			cnt=0;
			scanf("%d",&n);
			scanf("%s",s);
			for(i=1;i<=n;i++)
			{
				ans=ans+s[i-1]-'0';
			//	printf("%d\n",ans);
				if(i>ans)
				{
					x=i-ans;
					cnt=x+cnt;
					ans=x+ans;
				}
			//	printf("%d ",cnt);
			}
			printf("Case #%d: %d\n",k,cnt);
		}
		fclose(stdin);
    	fclose(stdout);
	}
	return 0;
} 
