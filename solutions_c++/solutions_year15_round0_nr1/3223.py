#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int n,t;
char ch[2000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int Case=1;t;t--,Case++) {
		printf("Case #%d: ",Case);
		scanf("%d",&n);
		scanf("%s",ch);
		int ans=0,sum=0;
		for (int i=0;i<=n;i++)
			if (ans+sum>=i) sum+=ch[i]-'0';
			else ans+=i-sum-ans,sum+=ch[i]-'0';
		printf("%d\n",ans);
	}
	return 0;
} 
