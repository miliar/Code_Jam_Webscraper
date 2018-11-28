/* ***********************************************
Author        :axp
Created Time  :2016/4/9 13:41:25
TASK		  :test.cpp
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

typedef long long ll;
const int N = (1<<16)+10;
int p[10000000];
int pn;
bool vis[N];
ll save[55][15];
int ans;

inline int ok(ll x)
{
	for(int i=0;1ll*p[i]*p[i]<=x;i++)
	{
		if(x%p[i]==0)return p[i];
	}
	return 0;
}

void work(int tx)
{
	int v;
	ll x=0;
	for(int base=2;base<=10;base++)
	{
		int ttx=tx;
		x=0;	
		for(ll i=1;ttx;i*=base)
		{
			if(ttx&1)x+=i;
			ttx>>=1;
		}
		v=ok(x);
		if(v==0)
		{
			return;
		}
		save[ans][base]=v;
	}
	save[ans++][1]=x;
}

int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

	for(int i=2;i<N;i++)
	{
		if(vis[i])continue;
		p[pn++]=i;
		for(int j=i<<1;j<N;j+=i)vis[j]=1;
	}

	//int t=77;
	//cout<<ok(t)<<endl;
	//work(35);
	//return 0;

	for(int i=N;i<1.1e8;i++)
	{
		//if(i>1.1e7)break;
		bool flag=1;
		for(int j=0;1ll*p[j]*p[j]<i;j++)
			if(i%p[j]==0)
			{
				flag=0;
				break;
			}
		if(flag)p[pn++]=i;
		if(i%1000000==0)printf("%d %d\n",i,pn);
	}
    for(int i=1<<15|1;i<(1<<16);i+=2)
	{
		work(i);
		if(ans==50)break;
	}
	puts("Case #1:");
	for(int i=0;i<ans;i++)
	{
		for(int j=1;j<=10;j++)
			printf("%lld%c",save[i][j],j==10?10:' ');
	}
    return 0;
}
