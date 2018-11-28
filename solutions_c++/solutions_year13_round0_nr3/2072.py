#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#define INF 1000000007
#define EPS 0.000000001
using namespace std;

int a[11111111];
int i,T,j;
long long k,p;

bool fair(long long x)
{
	int a[22];
	int n = 0;
	while(x>0)
	{
		a[n] = x%10;
		x/=10;
		n++;
	}
	for(int i=0;i<n/2;i++)
		if(a[i]!=a[n-1-i])
			return false;
	return true;
}

int main()
{
//	freopen("3.in","r",stdin);
//	freopen("3.out","w",stdout);
	a[0] = 0;
	for(i=1;i<=10000000;i++)
		if(fair(i) && fair((long long)i*i))
		{
			a[i] = a[i-1]+1;
//			printf("%d %I64d\n",i,(long long)i*i);
		}else
			a[i] = a[i-1];
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%I64d%I64d",&k,&p);
		printf("Case #%d: %d\n",t,a[int(sqrt(1.0*p))]-a[int(sqrt(k-1.0))]);
	}
	return 0;
}