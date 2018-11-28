#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <cmath>
#include <cstring>
using namespace std;
long long int solve(long long int arr[],long long int current,int pos,int n,long long int e,long long int r)
{
	if(pos>=n)
		return 0;
	else
	{
		long long int max=0;
		for(int i=0;i<=current;i++)
		{
			long long int send=current-i+r;
			if(send>e)
				send=e;
			long long int z=(arr[pos]*i)+solve(arr,send,pos+1,n,e,r);
			if(max<z)
				max=z;
		}
		return max;
	}
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int iter=0;iter<T;iter++)
	{
		long long int e,r,n,sol=0;
		scanf("%lld%lld%lld",&e,&r,&n);
		long long int arr[n];
		for(int i=0;i<n;i++)
			scanf("%lld",&arr[i]);
		if(r>=e)
		{
			for(int i=0;i<n;i++)
				sol+=(e*arr[i]);
		}
		else
		{
			long long int current=e;
			sol=solve(arr,current,0,n,e,r);
		}
		printf("Case #%d: %lld\n",iter+1,sol);
	}
}
