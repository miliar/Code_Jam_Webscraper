#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long int t,i=1;
	scanf("%lld",&t);
	while(i<=t)
	{
		string s;
		cin>>s;
		long long int l,j,k,count=0,swap=0;
		l=s.length();
		while(1)
		{
			for(j=l-1;j>=0;j--)
			{
				if(s[j]=='+')
				{
					l--;
				}
				else
				{
					break;
				}
			}
			if(l==0)
			{
				break;
			}
			swap=-1;
			for(k=0;k<l;++k)
			{
				if(s[k]=='+')
				{
					swap=k;
				}
				else{
					break;
				}
			}
			for(k=0;k<=swap;++k)
			{
				s[k]='-';
			}
			if(swap>=0)
			{
				count++;
			}
			for(k=0;k<l;++k)
			{
				if(s[k]=='+')
				{
					s[k]='-';
				}
				else
				{
					s[k]='+';
				}
			}
			count++;
		}
		
		
		
		
		
		printf("Case #%lld: %lld\n",i,count);
		i++;
	}
	return 0;
}
