/* ***********************************************
Author        :dingyuyang 
Created Time  :六  4/ 9 08:40:55 2016
File Name     :a.cpp
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
#define ll long long
const int inf=0x3f3f3f3f;
const ll llinf=0x3f3f3f3f3f3f3f3f;
const double finf=9999999999.0;
ll a;
int cnt[10];
ll solve()
{
	int flg=0,m=0;
	while(m<=1000000)
	{
		m++;
		ll b=a*m;
		do
		{
			int d=b%10;
			b/=10;
			cnt[d]++;
			if(cnt[d]==1) flg++;
			if(flg>=10) break;
		}while(b);
		if(flg>=10) break;
	}
	if(flg<10) return -1;
	else return a*m;
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout); 
	int t;
	scanf("%d",&t);
	for(int kase=1;kase<=t;kase++)
	{
		scanf("%lld",&a);
		memset(cnt,0,sizeof(cnt));
		ll ans=solve();
		if(ans==-1)
			printf("Case #%d: INSOMNIA\n",kase);
		else printf("Case #%d: %lld\n",kase,ans);
	}
    return 0;
}
