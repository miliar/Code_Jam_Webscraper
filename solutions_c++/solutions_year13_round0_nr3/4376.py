// File Name: c.cpp
// Author: Zlbing
// Created Time: 2013/4/13 13:37:44

#include<iostream>
#include<string>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
#include<cstring>
#include<stack>
#include<cmath>
#include<queue>
using namespace std;
#define CL(x,v); memset(x,v,sizeof(x));
#define INF 0x3f3f3f3f
#define LL long long
#define REP(i,r,n) for(int i=r;i<=n;i++)
#define RREP(i,n,r) for(int i=n;i>=r;i--)


LL G[100]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,0};

int main()
{
	int T;
	freopen("out1.txt","w",stdout);
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		LL a,b;
		scanf("%I64d %I64d",&a,&b);
		int ans=0;
		for(int i=0;G[i];i++)
		{
			if(G[i]>=a&&G[i]<=b)
				ans++;
			if(G[i]>b)
				break;
		}
		printf("Case #%d: %d\n",cas,ans);
	}
}
/*
const int MAXN=1e7;

LL a,ans;
int A[100];
bool solve(LL u)
{
	int len=0;
	while(u)
	{
		A[len++]=u%10;
		u=u/10;
	}
	bool flag=true;
	for(int i=0;i<len/2;i++)
		if(A[i]!=A[len-i-1])
		{
			flag=false;
			break;
		}
	return flag;
}
int main()
{
	freopen("out.txt","w",stdout);
	printf("G[]={1");
	for(LL i=2;i<=MAXN;i++)
	{
		a=(LL)i*i;
		if(solve(i)&&solve(a))
			printf(",%I64d",a);
	}
	printf("}");
    return 0;
}
*/
