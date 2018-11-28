/* ***********************************************
Author        :axp
Created Time  :2016/5/29 0:15:42
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

const int N = 200+10;
int T;
int n,k;
double ar[N];
double p[N];
double ans;
double dp[N][N<<1];
bool vis[N][N<<1];

double f(int now,int num)
{
	double &re=dp[now][num+N];
	if(vis[now][num+N])return re;
	vis[now][num+N]=1;

	if(now==k)return re= num==0;
	re=p[now]*f(now+1,num-1)+(1-p[now])*f(now+1,num+1);
	return re;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("lar.txt","w",stdout);
    cin>>T;
	for(int kase=1;kase<=T;kase++)
	{
		cin>>n>>k;
		for(int i=0;i<n;i++)
			cin>>ar[i];
		sort(ar,ar+n);
		ans=0;
		for(int i=0;i<=k;i++)
		{
			for(int j=0;j<k;j++)
				if(j<i)
					p[j]=ar[j];
				else
					p[j]=ar[j+(n-k)];
			memset(vis,0,sizeof vis);
			ans=max(ans,f(0,0));
		}
		printf("Case #%d: %.9lf\n",kase,ans);
	}
    return 0;
}
