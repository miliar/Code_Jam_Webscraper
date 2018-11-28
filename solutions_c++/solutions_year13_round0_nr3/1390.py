#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
using namespace std;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mod 1000000007
#define inf (1LL)<<60
typedef long long lld;
int pp[110];
int qq;
bool is(lld x)
{
	qq=0;
	while(x)
	{
		pp[qq++]=x%10;
		x/=10;
	}
	for(int i=0;i<qq;i++)
		if(pp[i] != pp[qq-i-1])
			return false;
	return true;
}
lld f[1000010];
int g;
void init()
{
	g=0;
	for(lld x=1;x<=10000000;x++)
	{
		if(is(x) && is(x*x))
			f[g++]=x*x;
	}
}
int main()
{
	init();
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		lld x,y;
		cin >> x >> y;
		int ans=0;
		for(int i=0;i<g;i++)
			if(x <= f[i] && f[i] <= y)
				ans++;
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
