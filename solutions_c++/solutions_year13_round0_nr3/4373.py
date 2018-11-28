// File Name: c.cpp
// Author: gonewithsin
// Created Time: 2013/4/13 22:33:47

#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<queue>
#include<map>
using namespace std;

long long p[45] =
{39,
1,4,9,121,484,
10201,12321,14641,40804,44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004
};
long long 

int T;

int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("out.out","w",stdout);	
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++)
	{
		long long x, y;
	   	int ax = -1, ay = -1;
		scanf("%I64d%I64d", &x, &y);
		for(int i = 1; i <= p[0]; i++)
			if(p[i] >= x)
			{
				ax = i;
				break;
			}
		for(int i = 1; i <= p[0]; i++)
			if(p[i] <= y)
			{
				ay = i;
			}
			else break;
		int ans = max(0, ay - ax + 1);
		printf("Case #%d: %d\n", cases, ans);
	}
    return 0;
}
