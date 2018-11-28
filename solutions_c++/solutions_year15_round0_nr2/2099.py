/* ***********************************************
Author        :axp
Created Time  :2015/4/11 11:09:59
File Name     :1.cpp
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const int maxn = 1010;
int T;
int n;
int ans;
int arr[maxn];
int sum[maxn];
int t;
int k;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

	scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
	{
		scanf("%d",&n);
		memset(arr,0,sizeof(arr));
		memset(sum,0,sizeof(sum));
		ans =0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&t);
			arr[t]++;
			ans=max(ans,t);
		}
		int x=ans;
		for(int i=2;i<x;i++)
		{
			for(int j=i+1;j<=x;j++)
			{
				sum[i]+=(j-1)/i*arr[j];
			}
			ans=min(ans,sum[i]+i);
		}
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}

