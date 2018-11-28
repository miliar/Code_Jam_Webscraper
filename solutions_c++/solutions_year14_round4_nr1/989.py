/* ***********************************************
Author        :kuangbin
Created Time  :2014/5/31 22:12:23
File Name     :E:\2014ACM\±ÈÈü\2014_GCJ_R2\A.cpp
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
int a[100010];
bool used[100010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
	int iCase = 0;
	int n,X;
	scanf("%d",&T);
	while(T--)
	{
		iCase++;
		scanf("%d%d",&n,&X);
		for(int i = 0;i < n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n);
		memset(used,false,sizeof(used));
		int id = n-1;
		int ans = 0;
		for(int i = 0;i < n;i++)
			if(!used[i])
		{
			while(id > i && a[i] + a[id] > X)id--;
			if(id > i)
			{
				used[id] = true;
				id--;
			}
			ans++;
			used[i] = true;
		}
		printf("Case #%d: %d\n",iCase,ans);
	}
    return 0;
}
