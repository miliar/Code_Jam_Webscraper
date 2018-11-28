#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
#define pb(x,y) x.push_back(y)
#define clr(x) memset(x,0,sizeof(x))

long long x[1100];

long long get(int a,long long M)
{
	int i;
	long long ans=0;

	for(i=1;i<=a;i++)
		ans+=M-x[i];
	for(;i<=37;i++)if(x[i]<=M)
		ans+=M+1-x[i];
	return ans;
}
long long BS(int a,long long B)
{
	int i,j;
	long long l,r,mid;

	l=x[a],r=x[36]-1;
	while(l<r)
	{
		mid=(l+r+1)/2;
		if(get(a,mid)<=B)
			l=mid;
		else
			r=mid-1;
	}
	return l;
}
int main()
{
	int t,i,j,k;
	long long B;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	cin>>t;
	int ii=0,n;
	while(t--)
	{
		cin>>B>>n;

		for(i=1;i<=n;i++)
			cin>>x[i];
		for(;i<=37;i++)
			x[i]=0;
		printf("Case #%d: ",++ii);
		sort(x+1,x+1+37);

		long double ans=0,tmp,tt=0;
		long long zong;

		for(i=1;i<=35;i++)
		{
			long long M=BS(i,B);
			if(M<0)
				continue;

			long long in=get(i,M);
			long long inc=0;

			if(in>B)
				continue;
			for(j=1;j<=i;j++)
				inc+=M-x[j];

			if(inc*36-in*i>ans*i)
				ans=inc*(36.0/i)-in;
		}
		printf("%.12llf\n",ans);
	}
}