#include<stdio.h>
int main()
{
	char str[100];
	int i,ans,t,c,c_,test,total,smax;
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		ans=0;
		total=0;
		scanf("%d",&smax);
		scanf("%s",str);
		for(i=0;i<smax;i++)
		{
			c=str[i]-'0';
			total=total+c;
			if(total<i+1 && str[i+1]>0)
			{
				ans=ans+(i+1)-(total);
				total=i+1;
				
				
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
