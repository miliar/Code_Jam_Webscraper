#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int t,cs=1;
	scanf("%d",&t);
	while(t--)
	{
		int min=1000,max=1000;
		char shr[2000];
		string s;
		//char shr;
		cin>>s;
		shr[min]=s[0];
		for(int i=1;s[i]!='\0';i++)
		{
			if(s[i]>=shr[min])
			{
				shr[--min]=s[i];
			}
			else
			shr[++max]=s[i];
		}
		printf("Case #%lld: ",cs++);
		for(int i=min;i<=max;i++)
		cout<<shr[i];
		cout<<endl;
	}
	return 0;
}
