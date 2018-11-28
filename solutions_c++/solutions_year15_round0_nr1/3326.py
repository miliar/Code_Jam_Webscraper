//CodejamA.cpp
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
#define ld long
#define F first
#define S second
#define ll long long
using namespace std;

char arr[1100];
int main()
{
	int t,co=1;
	scanf("%d",&t);
	while(t--)
	{
		int l;
		scanf("%d",&l);
		scanf("%s",arr);
		int i,sum=0,ans=0;
		for(i=0;i<=l;i++)
		{
			if(arr[i]==48) continue;
			if(sum<i)
			{
				ans+=(i-sum);
				sum=i;
			}
			sum=sum+arr[i]-48;
		}
		printf("Case #%d: %d\n", co++,ans);
	}
	return 0;	
}

