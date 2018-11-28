#include<stdio.h>
#include<string.h>

int main(void)
{
	int t,tt,ans,i;
	char s[105];
	freopen("input.txt","r",stdin);
	freopen("B_large.txt","w",stdout);
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%s",&s[1]);
		ans=0;
		for(i=1;i<strlen(&s[1]);i++)
		{
			if(s[i]!=s[i+1])
				ans++;
		}
		if(s[strlen(&s[1])]=='-')
			ans++;
		printf("Case #%d: %d\n",tt,ans);
	}
}