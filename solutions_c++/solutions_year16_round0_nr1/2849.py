/* ***********************************************
Author        :axp
Created Time  :2016/4/9 13:08:24
TASK		  :A.cpp
LANG          :C++
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
int st;

int f(int x)
{
	int re=0;
	while(x)
	{
		re|=1<<(x%10);
		x/=10;
	}
	return re;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		printf("Case #%d: ",kase);
		scanf("%d",&n);
		if(n==0)
		{
			puts("INSOMNIA");
			continue;
		}
		st=0;
		int now=0;
		while(st!=(1<<10)-1)
		{
			now+=n;
			st|=f(now);
		}
		printf("%d\n",now);
	}
    return 0;
}
