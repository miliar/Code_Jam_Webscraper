#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <map>

using namespace std;


int Solve(int *a, int max, int res, int n, int pos)
{
	if(pos == n)
	{
		if(max > a[n]) return res;
		else return res+1;
	}
	int ret;
	
	if(max>a[pos]) 
	{
		max += a[pos];
		ret = Solve(a, max, res, n, pos+1);
	}
	else 
	{
		int x = Solve(a, max, res+1, n, pos+1);
		if(max == 1) return x;

		while(max <= a[pos])
		{
			max += max-1;
			res++;
		}
		max += a[pos];
		int y = Solve(a, max, res, n, pos+1);
		ret = y<x ? y:x;
	}
	return ret;
}


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d",&T);

	for(int t = 1; t<=T; t++)
	{
		int A, N;
		int arr[101];
		scanf("%d %d",&A,&N);
		for(int i = 1; i<=N; i++)
		{
			scanf("%d",&arr[i]);
		}
		for(int i = 1; i<=N; i++)
		{
			for(int j = i+1; j<=N; j++)
			{
				if(arr[i]>arr[j])
				{
					int temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
		
		int res = 0;
		
		printf("Case #%d: %d\n",t,Solve(arr, A, 0, N, 1));
	}
}
