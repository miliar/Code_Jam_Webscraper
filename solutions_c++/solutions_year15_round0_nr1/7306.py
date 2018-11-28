#include<stdio.h>
#include<algorithm>
#include<map>
int main()
{
	int test,len;
	scanf("%d",&test);
	for(int p=1;p<=test;p++)
	{
		scanf("%d",&len);
		len++;
		char ip[len+1];
		scanf("%s",ip);
		int ans=0,tot=ip[0]-'0';
		for(int i=1;i<len;i++)
		{
			if(tot<i && ip[i]!='0')
			{
				ans+=i-tot;
				tot+=(i-tot);
			}
			tot+=ip[i]-'0';
		}
		printf("Case #%d: %d\n",p,ans);
	}
	return 0;
}
