/* ***********************************************
Author        :kuangbin
Created Time  :2014/5/31 23:13:50
File Name     :E:\2014ACM\±ÈÈü\2014_GCJ_R2\BLarge.cpp
************************************************ */

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
int a[1010];
bool cmp(int t1,int t2)
{
	return a[t1] < a[t2];
}
int b[1010];
int c[1010];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
	int iCase = 0;
	scanf("%d",&T);
	int n;
	while(T--)
	{
		iCase++;
		scanf("%d",&n);
		for(int i = 0;i < n;i++)
			scanf("%d",&a[i]);
		for(int i = 0;i < n;i++)b[i] = i;
		sort(b,b+n,cmp);
		for(int i = 0;i < n;i++)c[i] = 1;
		int ans = 0;
		for(int i = 0;i < n;i++)
		{
			int id = 0;
			for(int j = 0;j < b[i];j++)id += c[j];
			ans += min(id,(n-i)-1-id);
			c[b[i]] = 0;
		}
		printf("Case #%d: %d\n",iCase,ans);
	}
    return 0;
}

