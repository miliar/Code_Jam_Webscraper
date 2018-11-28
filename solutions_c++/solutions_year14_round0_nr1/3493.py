/* ***********************************************
Author        :kuangbin
Created Time  :2014/4/12 23:05:34
File Name     :E:\2014ACM\±ÈÈü\GCJ_Qua\A.cpp
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
bool used[20];

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
	scanf("%d",&T);
	int iCase = 0;
	while(T--)
	{
		iCase++;
		int r;
		scanf("%d",&r);
		int a;
		memset(used,false,sizeof(used));
		for(int i = 1;i <= 4;i++)
			for(int j = 1;j <= 4;j++)
			{
				scanf("%d",&a);
				if(i == r)
					used[a] = true;
			}
		int cnt = 0;
		int ans ;
		scanf("%d",&r);
		for(int i = 1;i <= 4;i++)
			for(int j = 1;j <= 4;j++)
			{
				scanf("%d",&a);
				if(i == r)
				{
					if(used[a])
					{
						cnt++;
						ans = a;
					}
				}
			}
		if(cnt == 0)
			printf("Case #%d: Volunteer cheated!\n",iCase);
		else if(cnt > 1)
			printf("Case #%d: Bad magician!\n",iCase);
		else printf("Case #%d: %d\n",iCase,ans);
	}


    return 0;
}
