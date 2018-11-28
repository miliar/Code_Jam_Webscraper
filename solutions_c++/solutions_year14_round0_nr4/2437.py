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
double a[N],b[N];
bool use[N];
int n;
int solve1()
{
	int tot=0;
	for (int i=1;i<=n;i++) use[i]=false;
	for (int i=1;i<=n;i++)
	{
		int t=1;
		while (t<=n&&(b[t]<a[i]||use[t])) t++;
		if (t<=n)
		{
			use[t]=true;
			tot++;
		}
		else
		{
			int t=1;
			while (use[t]) t++;
			use[t]=true;
		} 
	}
	return n-tot;
}
int solve2()
{
	int l1=1,l2=1,tot=0;
	for (int i=1;i<=n;i++)
	{
		if (a[l1]>b[l2])
		{
			l1++; l2++;
			tot++;
		}
		else l1++; 
	}
	return tot;
}
int main()
{
	//freopen("in.in","r",stdin);
	//freopen("out.out","w",stdout);
	int test=getint();
	for (int i=1;i<=test;i++)
	{
		n=getint();
		for (int i=1;i<=n;i++) scanf("%lf",&a[i]);
		for (int i=1;i<=n;i++) scanf("%lf",&b[i]);
		sort(&a[1],&a[n+1]); sort(&b[1],&b[n+1]);
		int ans1=solve1(),ans2=solve2();
		printf("Case #%d: %d %d\n",i,ans2,ans1);
	}
	return 0;
}
