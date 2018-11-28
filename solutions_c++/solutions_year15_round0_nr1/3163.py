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

char str[1100];
int main()
{
	int t,co=1;
	scanf("%d",&t);
	while(t--)
	{
		int len;
		scanf("%d",&len);
		scanf("%s",str);
		int i,sum=0,ans=0;
		for(i=0;i<=len;i++)
		{
			if(str[i]==48) continue;
			if(sum<i)
			{
				ans+=(i-sum);
				sum=i;
			}
			sum=sum+str[i]-48;
		}
		printf("Case #%d: %d\n", co++,ans);
	}
	return 0;	
}

