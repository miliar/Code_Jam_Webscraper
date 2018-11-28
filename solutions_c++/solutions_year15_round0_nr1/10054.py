#include<stdio.h>


int main()
{
	int T;
	scanf("%d",&T);
	
	for(int I=1;I<=T;I++)
	{
		int smax;
		scanf("%d",&smax);
		char s[smax+2];
		scanf("%s",s);
		
		int invite=0,people_till_now=s[0]-48;
		for(int i=1;i<=smax;i++)
		{
			int p=s[i]-48;
			if(people_till_now<i)
			{
				invite+=(i-people_till_now);
				people_till_now+=(i-people_till_now);
			}
			people_till_now+=p;
		}
		
		printf("Case #%d: %d\n",I,invite);
	}
}
