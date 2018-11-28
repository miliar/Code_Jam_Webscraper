/* ***********************************************
Author        :axp
Created Time  :2016/6/11 22:43:32
TASK		  :new.cpp
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

const int N = 2e4+10;
char ch[N];
int p[N][2];
int n;
int ans;

int main()
{
    freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
    int T;
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%s",ch+1);
		n=strlen(ch+1);
		for(int i=1;i<=n;i++)
			p[i][0]=i-1,p[i][1]=i+1;
		p[0][1]=1;
		ans=0;
		for(int i=1;i<=n;i++)
		{
			if(p[i][0]>=1 && ch[i]==ch[p[i][0]])
			{
				ans+=10;
				int lst=p[i][0];
				lst=p[lst][0];
				int nxt=p[i][1];
				p[nxt][0]=lst;
				p[lst][1]=nxt;
			}
		}
		int now=p[0][1];
		int num=0;
		while(now<=n)
		{
			num++;
			now=p[now][1];
		}
		ans+=num/2*5;
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}
