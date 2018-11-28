#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define N 1005
double a[N],b[N];
int n,bj[N];

void init()
{
	int i;
	cin>>n;
	FOR(i,1,n)
		cin>>a[i];
	FOR(i,1,n)
		cin>>b[i];
	sort(a+1,a+1+n);
	sort(b+1,b+1+n);
}

int deceitfulwar()
{
	int l,r,j,res=0;
	l=1;r=n;j=n;
	while(l<=r)
	{
		if(a[r]>b[j])
		{
			r--;
			res++;
		}else l++;
		j--;
	}
	return res;
}

int war()
{
	int i,flag,j,res=0;
	memset(bj,0,sizeof bj);
	FOR(i,1,n)
	{
		flag=0;
		FOR(j,1,n)
		{
			if(!bj[j] && b[j]>a[i])
			{
				bj[j]=1;
				flag=1;
				break;
			}
		}
		if(flag==0)res++;
	}
	return res;
}

int main()
{
	int i,T;
	cin>>T;
	FOR(i,1,T)
	{
		init();
		printf("Case #%d: %d %d\n",i,deceitfulwar(),war());
	}
}