#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;
bool can1(int n,long long less,long long p)
{
//	printf("%d %lld %lld\n",n,less,p);
	if(p==0)return 0;
	if(less==0)return 1;
	if(n==1)return p==2;
	if(p<=(1LL<<(n-1)))return 0;
	return can1(n-1,(less-1)/2,p-(1LL<<(n-1)));
}
bool can2(int n,long long grater,long long p)
{
	if(grater==0)return p>=(1LL<<n);
	if(n==1)return 1;
	if(p>=(1LL<<(n-1)))return 1;
	return can2(n-1,(grater-1)/2,p);
}
void solve()
{
	int n;
	long long p;
	scanf("%d %lld",&n,&p);
	long long l=0,r=(1LL<<n)-1;
//	can1(n,r,p);while(1);
	while(l<r)
	{
		long long mid=(l+r)/2+1;
		if(can1(n,mid,p))l=mid;
		else r=mid-1;
	}
	printf("%lld ",l);
	l=0,r=(1LL<<n)-1;
	while(l<r)
	{
		long long mid=(l+r)/2+1;
		if(can2(n,(1LL<<n)-1-mid,p))l=mid;
		else r=mid-1;
	}
	printf("%lld\n",l);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++cas);
		solve();
	}
}
