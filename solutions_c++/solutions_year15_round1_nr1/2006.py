#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<bitset>
#include<time.h>
#define ll __int64
#define inf 0x7FFFFFFF
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
const double eps=1e-9;
const double pi=acos(-1.0);
const int mod=1000000007;
int a[10001];
int main()
{
    freopen("A-large.in","r",stdin);freopen("A-output-large.txt","w",stdout);
	int i,j,t,tt=0,n,mx,tmp,ans1,ans2;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",a+i);
		ans1=0;
		mx=0;
		for(i=1;i<n;i++)
		{
			tmp=max(a[i-1]-a[i],0);
			mx=max(tmp,mx);
			ans1+=tmp;
		}
		ans2=0;
		for(i=0;i<n-1;i++)
		{
			ans2+=min(mx,a[i]);
		}
		printf("Case #%d: %d %d\n",++tt,ans1,ans2);
	}
	return 0;
}
/*
99
4
10 5 15 5
2
100 100
8
81 81 81 81 81 81 81 0
6
23 90 40 0 100 9

Case #1: 15 25
Case #2: 0 0
Case #3: 81 567
Case #4: 181 244
*/
