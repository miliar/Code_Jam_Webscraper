/* ***********************************************
Author        :kuangbin
Created Time  :2014/4/12 23:33:53
File Name     :E:\2014ACM\±ÈÈü\GCJ_Qua\B.cpp
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

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
	int iCase = 0;
	scanf("%d",&T);
	while(T--)
	{
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double ans = X/2;
		double tmp = 0;
		double add = 2;
		while(1)
		{
			tmp += C/add;
			add += F;
			ans = min(ans,tmp + X/add);
			if(tmp - ans > 1e-8)
				break;
		}
		iCase++;
		printf("Case #%d: %.7lf\n",iCase,ans);
	}
    return 0;
}
