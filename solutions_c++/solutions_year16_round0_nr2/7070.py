#include<stdio.h>
int main(void)
{
	int t,i,l,j,c;
	char s[100];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		c=0,j=0;
		scanf("%s",&s);
		for(l=0;s[l]!='\0';++l);
	//	printf("%d",l);
		
	if(s[j]=='+')
		{
			while(s[j]=='+')
			++j;
			
			if (j==l)
			goto x;
			
			while(s[j]=='-')
			++j;
			c=2;
		}
		
		if(s[j]=='-')
		{
			while(s[j]=='-')
			++j;
			
			while(s[j]=='+')
			++j;
			
			c=1;
			}	
		while(j<l)
		{
			
		if(s[j]=='+')
		{
		
			while(s[j]=='+')
			++j;}
		if(s[j]=='-')
			{
		while(s[j]=='-')
			++j; c=c+2;
			}
			
		}
		x: printf("Case #%d: %d\n",i,c); 
	}
	return 0;
}
