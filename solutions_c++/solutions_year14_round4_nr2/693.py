#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define FOR(i,j,k) for(i=j;i<=k;++i)
#define FORD(i,j,k) for(i=j;i>=k;i--)
#define inf 0x7fffffff
#define N 1004
int n,res,a[N];

void init()
{
	int i;
	scanf("%d",&n);
	FOR(i,1,n)scanf("%d",a+i);
}

int work()
{
	int mm,l=1,r=n,i,ans=0,ij;
	while(l<r)
	{
		mm=inf;
		FOR(i,l,r)
		{
			if(a[i]<mm)
			{
				mm=a[i];
				ij=i;
			}
		}
		if(ij-l<r-ij)
		{
			ans+=ij-l;
			FORD(i,ij,l+1)swap(a[i],a[i-1]);
			l++;
		}else
		{
			ans+=r-ij;
			FOR(i,ij,r-1)swap(a[i],a[i+1]);
			r--;
		}
	}
	return ans;
}

int main()
{
	int i,t;
	scanf("%d",&t);
	FOR(i,1,t)
	{
		init();
		printf("Case #%d: %d\n",i,work());
	}
}