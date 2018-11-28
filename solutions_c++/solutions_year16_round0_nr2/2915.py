/* ***********************************************
Author        :axp
Created Time  :2016/4/9 13:27:31
TASK		  :B.cpp
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

const int N = 105;
int T;
char ch[N];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%s",ch);
		int now;
		int ans=0;
		for(now=1;ch[now];now++)
			if(ch[now]!=ch[now-1])
				ans++;
		if(ch[now-1]=='-')ans++;
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}
