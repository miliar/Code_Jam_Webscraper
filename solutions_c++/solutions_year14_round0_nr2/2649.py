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
typedef long double LD;
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
void solve(int id,LD C,LD F,LD X)
{
	LD ans=1e6,V=2,T=0;
	for (int i=0;i<=X;i++)
	{
		ans=min(ans,T+X/V);
		T+=C/V; V+=F;
	}
	printf("Case #%d: %.8lf\n",id,(double)ans);
	return ;
}
int main()
{
//	freopen("in.in","r",stdin);
//	freopen("out.out","w",stdout);
	int test=getint();
	for (int i=1;i<=test;i++)
	{
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		solve(i,C,F,X);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
