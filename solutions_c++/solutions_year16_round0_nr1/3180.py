/* ***********************************************
Author        :yzkAccepted
Created Time  :2016/4/9 17:40:48
TASK		  :ggfly.cpp
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
#include <stack>
using namespace std;
typedef __int64 ll;
int vis[10],flag;
void check(int n)
{
	int k;
	while(n)
	{
		k=n%10;
		vis[k]=1;
		n=n/10;
	}
	for(int i=0;i<=9;i++)
	{
		if(vis[i]==0)
			break;
		if(vis[i]==1 && i==9)
			flag=1;
	}
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,t,cas=1;
	scanf("%d",&t);
	while(t--)
	{
		memset(vis,0,sizeof(vis));
		scanf("%d",&n);
		printf("Case #%d: ",cas);
		cas++;
		if(n==0)
			printf("INSOMNIA\n");
		else
		{
			flag=0;
			int y=n;
			int tot=0;
			check(n);
			while(flag==0)
			{
				y=y+n;
				check(y);
				if(flag==1)
					break;
			}
			printf("%d\n",y);
		}
	}
    return 0;
}
