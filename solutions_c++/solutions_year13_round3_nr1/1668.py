#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<set>
#include<vector>
#include<list>
#include<stack>
#include<map>
#include<algorithm>
#include<functional>
#include<string>
typedef unsigned long long ulli;
using namespace std;

void doit()
{
	int i,j,n;
	string s;
	cin>>s>>n;
	int count=0;
	for(i=0;i<=s.length()-n;i++)
	{
		for(j=s.length()-1;j>=i+n-1;j--)
		{
			int f=0;
			for(int t=i;t<=j;t++)
			{
				if(s[t]=='a' || s[t]=='e' || s[t]=='i' || s[t]=='o' || s[t]=='u')
					f=0;
				else
					f++;
				if(f>=n)
					break;
			}
			if(f>=n)
				count++;
			else
				break;
		}
	}
	printf("%d",count);
}
int main()
{
	int c,t;
	
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	scanf("%d",&t);
	for(c=1;c<=t;c++)
	{	
		printf("Case #%d: ",c);
		doit();
		printf("\n");
	}
	return 0;
}
