#include<stdio.h>
int main()
{
	int n,t,i,test,c,tmp;
	char S[1001];
	scanf("%d",&t);
	for(test=1;test<=t;test++)
	{
		scanf("%d%s",&n,S);
		c=tmp=0;
		for(i=0;S[i];i++)
		{
			if((tmp<i)&&S[i]!=48)
			{
				c+=i-tmp;
				tmp+=c;
			}
			tmp+=S[i]-48;
		}
		printf("Case #%d: %d\n",test,c);
	}
	return 0;
}
