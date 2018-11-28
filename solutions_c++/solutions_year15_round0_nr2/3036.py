#include <stdio.h>
#include <vector>
#include <queue>
#include <string.h>
#include <stdlib.h>
#include <cstdio>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <limits.h>
#define llu long long unsigned
#define ld long
#define F first
#define S second
#define ll long long
using namespace std;

int arr[1100];
int main()
{
	int t,co=1;
	scanf("%d",&t);
	while(t--)
	{
		int i,D,j,temp,ans=100000;
		scanf("%d",&D);
		for(i=0;i<D;i++)
			scanf("%d",&arr[i]);
	
		for(i=1;i<=1000;i++)
		{	
			temp=0;
			for(j=0;j<D;j++)
			{
				if(arr[j]>i)
				{
					if(arr[j]%i==0)
						temp+=(arr[j]/i-1);
					else
						temp+=(arr[j]/i);
				}
			}
			ans=min(ans,i+temp);
		}
		printf("Case #%d: %d\n", co++,ans);
	}
	return 0;	
}

