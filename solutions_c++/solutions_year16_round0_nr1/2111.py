/*
* Filename:    A.cpp
* Desciption:  A
* Created:     2016年04月09日 13时41分08秒 星期六
* Author:      JIngwei Xu [mail:xu_jingwei@outlook.com]
*
*/
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;

//Init Const
const int INF=1e9;
const int maxn=1e6+7;

//Global Variables
int n,ans,finalnum,t;
bool vis[12];
//Function Declaration
void solve(int x,int t);

//Main Program
int main()
{
#ifdef AC_THIS_PROBLEM
	freopen("A-small-attempt0.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
	//Init
	
	
	
	//Input
	scanf("%d",&t);
	for (int i = 1; i <=t; i += 1)
	{
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",i);
		}else{
			ans=0;
			memset(vis,false,sizeof(vis));
			solve(n,1);
			printf("Case #%d: %d\n",i,finalnum);
		}
	}
	return 0;
}
void solve(int x,int t){
	if(t>1000){
		printf("FUCK\n");
		return;
	}
	int y=t*x;
	char s[10];
	sprintf(s,"%d",y);
	for (int i = 0; i < 8; i += 1)
	{
		int t=s[i]-'0';
		
		if(t>=0&&t<=9&&!vis[t]){
			vis[t]=true;
			ans++;
			if(ans==10){
			finalnum=y;
			return;
			}
		}
	}
	solve(x,t+1);
}
