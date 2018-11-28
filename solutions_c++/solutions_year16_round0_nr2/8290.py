#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<string>
using namespace std;
int main()
{
//	freopen("B.in","r",stdin);
//	freopen("B.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		string s;
		cin>>s;
		int len=s.size();
		int ans=0;
		for(int i=0;i<len-1;i++)if(s[i]!=s[i+1])ans++;
		if(s[len-1]=='-')ans++;
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
