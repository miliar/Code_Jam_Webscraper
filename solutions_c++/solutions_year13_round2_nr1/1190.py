#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <cmath>
#include <cstring>
using namespace std;
long int dp(long int arr[],long int current,long long int A,long int N)
{
	if(current==N)
		return 0;
	if(A>arr[current])
	{
		return dp(arr,current+1,A+arr[current],N);
	}
	else
	{
		if(2*A-1==A)
			return (N-current);
		else
			return min(dp(arr,current,2*A-1,N)+1,N-current);
	}
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int iter=0;iter<T;iter++)
	{
		long int A,N;
		scanf("%ld%ld",&A,&N);
		long int arr[N];
		for(int i=0;i<N;i++)
		{
			scanf("%ld",&arr[i]);
		}
		sort(arr,arr+N);
		long int res=dp(arr,0,A,N);
		printf("Case #%d: %ld\n",iter+1,res);
	}
}
