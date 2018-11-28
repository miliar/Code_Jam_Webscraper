/* ***********************************************
Author        :axp
Created Time  :2015/4/11 10:39:53
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

int T;
int n;
int x;
int now,sum;
int ans;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%d",&n);
		getchar();
		now=0;
		ans=0;
		for(int i=0;i<=n;i++)
		{
			x=getchar()-'0';
			if(i>now)
			{
				ans+=i-now;
				now=i;
			}
			now+=x;
		}
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}
