/* ***********************************************
Author        :kuangbin
Created Time  :2014/4/13 2:14:21
File Name     :E:\2014ACM\±ÈÈü\GCJ_Qua\D.cpp
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
double a[1010];
double b[1010];
bool used[1010];
bool used2[1010];
int c[1010];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
	int iCase = 0;
	int T;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		memset(used,false,sizeof(used));
		memset(used2,false,sizeof(used2));
		for(int i = 0;i < n;i++)
			scanf("%lf",&a[i]);
		for(int i = 0;i < n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		int ans1 = 0,ans2 = 0;
		for(int i = 0;i < n;i++)
			c[i] = i;
		int tt = 0;
		do
		{
			memset(used,false,sizeof(used));
			memset(used2,false,sizeof(used2));
			int cnt1 = 0;
			int cnt2 = 0;
			for(int i = 0;i < n;i++)
			{
				int Max = -1;
				for(int j = 0;j < n;j++)
					if(!used[j] &&  a[c[i]] > b[j] && (Max == -1 || b[Max] > b[j]))
						Max = j;
				if(Max == -1)
				{
					int Min = -1;
					for(int j = 0;j < n;j++)
						if(!used[j] && (Min == -1 || b[Min] < b[j]))
							Min = j;
					used[Min] = true;
				}
				else
				{
					cnt1++;
					used[Max] = true;
				}
			}

			for(int i = 0;i < n;i++)
			{
				int Max = -1;
				for(int j = 0;j < n;j++)
					if(!used2[j] && a[c[i]] < b[j] && (Max == -1 || b[Max] > b[j]))
						Max = j;
				if(Max == -1)
				{
					int Min = -1;
					for(int j = 0;j < n;j++)
						if(!used2[j] && (Min == -1 || b[Min] > b[j]))
							Min = j;
					used2[Min] = true;
					cnt2++;
				}
				else
				{
					used2[Max] = true;
				}
			}
			ans1 = max(ans1,cnt1);
			ans2 = max(ans2,cnt2);
			tt++;
			reverse(c,c+n);
			if(tt >= 2)
				break;
		}
		while(1);
		//while(next_permutation(c,c+n));
		iCase++;
		printf("Case #%d: %d %d\n",iCase,ans1,ans2);
	}
    return 0;
}
