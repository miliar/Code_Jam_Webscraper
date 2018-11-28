#include<stdio.h>
#define li long int
char str[10004];
int main()
{
	int t,ca=0;
	scanf("%d",&t);
	while(t--)
	{
		li n,ans=0,ctr=0;
		scanf("%d%s",&n,&str);
		for(li i=0;str[i]!='\0';i++)
		{	
			if(i>ctr)
			{
				li temp=0;
				while(i>ctr)
				{
					ans++;  ctr++;
				}
				ctr+=((int)str[i]-48);
	
			}
			else
			ctr+=((int)str[i]-48);
		}
		printf("Case #%d: %ld\n",++ca,ans);
	}
	return 0;
}
