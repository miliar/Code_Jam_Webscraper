#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		char s[105];
		scanf("%s",s);
		int l=strlen(s);
		stack<char> dp;
		for(int i=0;i<l;i++)
		{
			if(dp.empty()) dp.push(s[i]);
			else
			{
				char ch=dp.top();
				if(s[i]!=ch) dp.push(s[i]);
			}
		}
		char ch=dp.top();
		if(ch=='+') dp.pop();
		printf("Case #%d: %d\n",c,dp.size());
	}
return 0;
}
