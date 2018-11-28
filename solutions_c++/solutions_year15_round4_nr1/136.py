/* ***********************************************
Author        :kuangbin
Created Time  :2015/5/30 21:59:30
File Name     :F:\ACM\2015ACM\±»»¸¡∑œ∞\2015GCJ_R2\A.cpp
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
char str[110][110];
int num1[110],num2[110];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
	int iCase = 0;
	scanf("%d",&T);
	while(T--){
		iCase++;
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i = 0;i < n;i++)
			scanf("%s",str[i]);
		memset(num1,0,sizeof(num1));
		memset(num2,0,sizeof(num2));
		for(int i = 0;i < n;i++)
			for(int j = 0;j < m;j++)
				if(str[i][j] != '.'){
					num1[i]++;
					num2[j]++;
				}
		int ans = 0;
		bool flag = true;
		for(int i = 0;i < n;i++)
			for(int j = 0;j < m;j++){
				if(!flag)break;
				if(str[i][j] == '.')continue;
				if(num1[i] == 1 && num2[j] == 1){
					flag = false;
					break;
				}
				int dx,dy;
				if(str[i][j] == '^'){
					dx = -1;
					dy = 0;
				}
				else if(str[i][j] == '>'){
					dx = 0;
					dy = 1;
				}
				else if(str[i][j] == '<'){
					dx = 0;
					dy = -1;
				}
				else {
					dx = 1;
					dy = 0;
				}
				int x = i;
				int y = j;
				bool has = false;
				x += dx;
				y += dy;
				while(x >= 0 && x < n && y >= 0 && y < m){
					if(str[x][y] != '.')has = true;
					x += dx;
					y += dy;
				}
				if(!has)ans++;
			}
		if(!flag)printf("Case #%d: IMPOSSIBLE\n",iCase);
		else printf("Case #%d: %d\n",iCase,ans);
	}
    return 0;
}
