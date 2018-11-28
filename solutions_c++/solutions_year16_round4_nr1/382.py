/* ***********************************************
Author        :axp
Created Time  :2016/5/28 22:11:06
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

const int N = 15;
int ar[N][3];
string dp[3][N];
bool vis[3][N];
int T;
int n,c[3];
char mp[10]="RPS";

bool ok()
{
	int tmp[2][3];
	for(int i=0;i<3;i++)
	{
		tmp[0][i]=ar[n][i];
		tmp[1][i]=c[i];
	}
	sort(tmp[0],tmp[0]+3);
	sort(tmp[1],tmp[1]+3);
	for(int i=0;i<3;i++)
		if(tmp[0][i]!=tmp[1][i])
			return 0;
	return 1;
}

string f(int win,int x)
{
	string &s=dp[win][x];
	if(vis[win][x])return s;
	vis[win][x]=1;
	if(x==0)return s=mp[win];
	s=f(win,x-1)+f((win-1+3)%3,x-1);
	s=min(s,f((win-1+3)%3,x-1)+f(win,x-1));
	return s;
}

void solve()
{
	if(ok()==0)
	{
		puts("IMPOSSIBLE");
		return;
	}
	int se=0;
	for(int i=0;i<3;i++)
	{
		int t=0;
		for(int j=0;j<3;j++)
			if(c[i]==c[j])
				t++;
		if(t==1)se=i;
	}

	int win=((se-n)%3+3)%3;
	//cout<<win<<endl;
	string s=f(win,n);
	cout<<s<<endl;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ar[0][2]=1;
	for(int i=1;i<N;i++)
	{
		for(int j=0;j<3;j++)
			ar[i][(j+1)%3]=ar[i-1][j]+ar[i-1][(j+1)%3];
		//sort(ar[i],ar[i]+3);
		//cout<<ar[i][0]<<' '<<ar[i][1]<<' '<<ar[i][2]<<endl;
	}
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%d",&n);
		for(int i=0;i<3;i++)
			scanf("%d",&c[i]);
		printf("Case #%d: ",kase);
		solve();
	}
    return 0;
}
