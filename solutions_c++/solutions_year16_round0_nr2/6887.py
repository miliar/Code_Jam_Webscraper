#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	long long t,cs=1;
	scanf("%lld",&t);
	while(t--)
	{
		string s;
		int a[100]={0},l=0,i=0;
		cin>>s;
		while(s[i]!='\0')
		{
			if(s[i]=='+')
			{
				a[l++]=1;
				while(s[i]=='+'&&s[i]!='\0')
				{
					i++;
					if(s[i]=='\0')
					goto label;
				}
			}
			if(s[i]=='-')
			{
				a[l++]=0;
				while(s[i]=='-'&&s[i]!='\0')
				{
					i++;
					if(s[i]=='\0')
					goto label;
				}
			}
		}
		label:;
		printf("Case #%lld: ",cs++);
		int vai=0;
		if(a[0]==1&&l%2!=0)
		printf("%lld\n",l-1);
		else if(a[0]==1&&l%2==0)
		printf("%lld\n",l);
		else if(a[0]==0&&l%2!=0)
		printf("%lld\n",l);
		else if(a[0]==0&&l%2==0)
		printf("%lld\n",l-1);
	}
	return 0;
}
