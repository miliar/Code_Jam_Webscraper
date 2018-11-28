/* ***********************************************
Author        :dingyuyang 
Created Time  :六  4/ 9 08:13:25 2016
File Name     :b.cpp
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
char s[200];
int ans;
void solve()
{
	int sz=strlen(s);
	int ptr=sz-1;
	int d=0;
	while(ptr>=0)
	{
		int flg;
		if(s[ptr]=='-') flg=1;
		else flg=0;
		int cnt=flg+d;
		if((cnt&1)==1)
		{
			d++;
			ans++;
		}
		ptr--;
	}
}
int main()
{
    freopen("B-large.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int kase=1;kase<=t;kase++)
	{
		scanf("%s",s);
		ans=0;
		solve();
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}
