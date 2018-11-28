#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#define maxn 1010
using namespace std;
int ans;
void read()
{
	static char str[maxn];
	int n;
	scanf("%d %s",&n,str);
	ans=0;
	for(int i=0,sum=0;i<=n;++i)
	{
		ans=max(ans,i-sum);
		sum+=str[i]-'0';
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,C=0;
	for(cin>>T;T;--T)
	{
		read();
		printf("Case #%d: %d\n",++C,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
