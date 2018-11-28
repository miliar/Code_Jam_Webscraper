#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;
const long long LINF = ~(((long long)0x1)<<63)/2;
const int INF=0X3F3F3F3F;
typedef long long LL;
int T,n;
LL P;
int main()
{
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out.txt","w",stdout);
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++)
	{
		scanf("%d%lld",&n,&P);
		printf("Case #%d: ",ca);
		LL lo=-1,up=(1LL<<n);
		while(lo+1<up)
		{
			LL mid=(lo+up)/2;
			LL win=mid,lose=(1LL<<n)-1-win;
			LL ret=0;
			for(int i=n-1;i>=0;i--)
			{
				if(win!=0)
				{
					win--;
					ret+=(1LL<<i);
					if(lose%2==1)lose=lose/2+1;
					else lose/=2;
					win/=2;
				}
				else
				{
					lose/=2;
				}
			}
			if(ret>=P)up=mid;
			else lo=mid;
		}
		printf("%lld ",lo);
		lo=-1,up=(1LL<<n);
		while(lo+1<up)
		{
			LL mid=(lo+up)/2;
			LL win=mid,lose=(1LL<<n)-1-win;
			LL ret=0;
			for(int i=n-1;i>=0;i--)
			{
				if(lose!=0)
				{
					lose--;
					if(win%2==1)win=win/2+1;
					else win/=2;
					lose/=2;
				}
				else
				{
				    ret+=(1LL<<i);
					win/=2;
				}
			}
			if(ret>=P)up=mid;
			else lo=mid;
		}
		printf("%lld\n",lo);
	}
}
