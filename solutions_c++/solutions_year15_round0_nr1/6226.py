#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int t,n=1;
	scanf("%d",&t);
	while(t--)
	{
		int l,a,c=0,sum=0,add;
		scanf("%d",&l);
		string s1;
		cin>>s1;
		if(s1[0]-'0'==0)	
		{	
			sum++;
			c++;
		}
		for(a=1;a<l+1;a++)
		{
			sum+=s1[a-1]-'0';
			if(s1[a]-'0'==0)
			{	
				while(s1[a]-'0'==0)
				a++;
				if(a>sum)
				{
					add=a-sum;
					c+=add;
					sum+=add;
				}
			}
		}	
		printf("Case #%d: %d\n",n,c);
		n++;
	}
}


