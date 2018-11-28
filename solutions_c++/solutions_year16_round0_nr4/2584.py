/* ***********************************************
Author        :yzkAccepted
Created Time  :2016/4/9 20:32:55
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

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll n,t,k,c,i,j,cas=1,s;
	scanf("%I64d",&t);
	while(t--)
	{
		scanf("%I64d%I64d%I64d",&k,&c,&s);
		printf("Case #%I64d: ",cas);
		cas++;
		ll cmp=1;
		for(i=1;i<=c-1;i++)
		{
			cmp=k*cmp;
		}
		ll ans;
		for(i=0;i<s;i++)
		{
			ans=i*cmp+1;
			if(i!=s-1)
				printf("%I64d ",ans);
			else
				printf("%I64d\n",ans);
		}
	}
    return 0;
}
