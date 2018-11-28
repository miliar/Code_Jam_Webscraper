#include<stdio.h>
int main()
{	int t,s,j,i,n=1,sum=0,count=0;
	char ch[100];
	scanf("%d",&t);
	while(t--)
	{
		scanf("\n%d ",&s);
		gets(ch);
		sum=0;
		count=0;
		if(s%2!=0)
		{
		for(i=0;i<s;i++)
		{	j=i+1;
			sum+=ch[i]-48;
			if(sum<j)
			{
			count++;
			sum++;
		}
		}
	}
	else 
		{
		for(i=0;i<=s;i++)
		{	j=i+1;
			sum+=ch[i]-48;
			if(sum<j)
			{
			count++;
			sum++;
		}
		}
	}
		printf("\nCase #%d: %d\n",n,count);
		n++;
	}
	return 0;
}
