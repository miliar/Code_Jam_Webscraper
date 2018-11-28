#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#define FOR(i,j,k) for(i=j;i<=k;++i)
#define N 10004
int a[N],b[N];

bool comp(int i,int j)
{
	return i>j;
}

int work()
{
	int i,ans,bj,j,n,x;
	scanf("%d%d",&n,&x);
	FOR(i,1,n)scanf("%d",a+i);
	sort(a+1,a+1+n,comp);
	ans=0;
	FOR(i,1,n)
	{
		bj=0;
		FOR(j,1,ans)
		{
			if(b[j]==-1)break;
			if(b[j]+a[i]<=x)
			{
				b[j]=-1;
				bj=1;
				break;
			}
		}
		if(!bj)b[++ans]=a[i];
		sort(b+1,b+1+ans,comp);
	}
	return ans;
}

int main()
{
	int i,T;
	scanf("%d",&T);
	FOR(i,1,T)
	{
		printf("Case #%d: %d\n",i,work());

	}
}