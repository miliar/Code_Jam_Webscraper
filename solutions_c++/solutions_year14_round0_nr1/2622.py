#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include<string>
#include<ctime>
#include<cmath>
#include<utility>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#define INF 1111111111
#define N 11111
#define eps 1e-9
using namespace std;
typedef long long LL;
int getint()
{
	char ch;
	do
	{
		ch=getchar();
	}while (ch!='-'&&(ch<'0'||ch>'9'));
	int ans=0,f=0;
	if (ch=='-') f=1; else ans=ch-'0';
	while (isdigit(ch=getchar())) ans=ans*10+ch-'0';
	if (f) ans*=-1;
	return ans;
}
int vis[22];
void solve(int x)
{
	int a,b,tot=0,ans;
	a=getint();
	for (int i=1;i<=4;i++)
	for (int j=1;j<=4;j++)
	{
		int t=getint();
		if (i==a) vis[t]=x;
	}
	b=getint();
	for (int i=1;i<=4;i++)
	for (int j=1;j<=4;j++)
	{
		int t=getint();
		if (i==b&&vis[t]==x) tot++,ans=t;
	}
	printf("Case #%d: ",x);
	if (tot>1) printf("Bad magician!\n");
	else if (tot==1) printf("%d\n",ans);
	else printf("Volunteer cheated!\n");
	return ;
}
int main()
{
//	freopen("in.in","r",stdin);
//	freopen("out.out","w",stdout);
	int test=getint();
	for (int i=1;i<=test;i++) solve(i);
	return 0;
}
