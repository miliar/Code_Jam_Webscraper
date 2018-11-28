#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("l.txt","wb",stdout);
	int data;
	scanf("%d",&data);
	for(int p=1;p<=data;p++)
	{
		string s;
		cin>>s;
		int n;
		scanf("%d",&n);
		int c=0;
		for(int i=0;i<int(s.size())-n+1;i++)
		{
			if(s[i]=='-')
			{
				for(int j=0;j<n;j++)
				{
					if(s[i+j]=='+')s[i+j]='-';
					else s[i+j]='+';
				}
				c++;
			}
		}
		bool f=true;
		for(int i=0;i<s.size();i++)if(s[i]!='+')f=false;
		printf("Case #%d: ",p);
		if(!f)printf("IMPOSSIBLE\n");
		else printf("%d\n",c);
	}
}