#include<iostream>
#include<stdio.h>
#include<string.h>
char str[10005];
int main()
{
	int t,cse=0;
	scanf("%d",&t);
	while(t--)
	{
		long int n,res=0,count=0,i;
		scanf("%ld%s",&n,str);
		long int len =strlen(str);
		for(i=0;i<len;i++)
		{	
			if(i>count)
			{
				long int temp=0;
				while(i>count)
				{
					res++;  count++;
				}
				count+=((int)str[i]-48);
	
			}
			else
			{
			count+=((int)str[i]-48);
			}
			
		}
		printf("Case #%d: %ld\n",++cse,res);
	}
	return 0;
}
