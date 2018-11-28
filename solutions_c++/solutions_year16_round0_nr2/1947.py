#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long LL;
char ch[10000];
int n,numcase,ans;
int main()
{
	freopen("bb.in","r",stdin);
	freopen("bb.out","w",stdout);
	int numcase;
	cin>>numcase;
	for(int ii=1;ii<=numcase;ii++)
	{
		int ans=0;
		scanf("%s",ch+1);
		int n = strlen(ch+1);
		for(int i=1;i<n;i++)
			if(ch[i] != ch[i+1]) ans++;
		if(ch[n]=='-') ans++;
		printf("Case #%d: %d\n",ii,ans);
	}
}
