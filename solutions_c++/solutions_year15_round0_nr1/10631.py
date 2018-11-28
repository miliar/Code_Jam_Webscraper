#include<stdio.h>
#include<string.h>

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test,max,std,fr,st;

	scanf("%d\n",&test);
	for(int i=1;i<=test;i++)
	{
		char str[200],ch;
		std=0;
		fr=0;
		scanf("%d",&max);
		scanf("%c",&ch);
		gets(str);
		for(int j=0;j<=max;j++)
		{
			 
				
			if(str[j]!='0')
			{
		     
			 st=str[j]-'0';
			if(std<j)
			{
				fr+=j-std;
				std+=fr+st;
			}
			else
			{
				std+=st;
			}
			}
		}
		 
		printf("Case #%d: %d\n",i,fr);
	}
	
	return 0;
}