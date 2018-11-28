#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long LL;
#include <queue>

int dis[1000005];

int reverse(int x)
{
	int ans=0;
	while(x)
	{
		ans=ans*10+x%10;
		x/=10;
	}
	return ans;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	for(int i=1;i<=1000000;i++)
		dis[i]=INT_MAX/2;
	dis[1]=1;
	queue<int> q;
	q.push(1);
	while(!q.empty())
	{
		int x=q.front();
		q.pop();
		if(x+1<=1000000 && dis[x+1]>dis[x]+1)
		{
			dis[x+1]=dis[x]+1;
			q.push(x+1);
		}
		int rev=reverse(x);
		if(rev<=1000000 && dis[rev]>dis[x]+1)
		{
			dis[rev]=dis[x]+1;
			q.push(rev);
		}
	}
	int T, ca=1;
	scanf("%d",&T);
	while(T--)
	{
		int tmp;
		scanf("%d",&tmp);
		printf("Case #%d: %d\n", ca++, dis[tmp]);
	}
    return 0;
}
