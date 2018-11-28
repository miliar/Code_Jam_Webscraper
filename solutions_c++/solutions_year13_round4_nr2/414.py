#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define inf 0xfffffff
typedef long long lld;
#define eps 1e-8
#define pi acos(-1.0)
int n;
lld total;
lld p;
lld solve_one(lld m)
{
	lld now=1;
	lld step=total/2;
	while(step)
	{
		if(m >= 1)
		{
			now+=step;
			m--;
			m/=2;
		}
		else
			;
		step/=2;
	}
	return now;
}
lld one()
{
	lld l=0;
	lld r=total-1;
	lld ans=0;
	while(r >= l)
	{
		lld m=(l+r)/2;
		if(solve_one(m) <= p)
		{
			ans=m;
			l=m+1;
		}
		else
			r=m-1;
	}
	return ans;
}
lld solve_two(lld m)
{
	m=total-m-1;
	lld now=1;
	lld step=total/2;
	while(step)
	{
		if(m >= 1)
		{
			m--;
			m/=2;
		}
		else
			now+=step;
		step/=2;
	}
	return now;
}
lld two()
{
	lld l=0;
	lld r=total-1;
	lld ans=0;
	while(r >= l)
	{
		lld m=(l+r)/2;
		if(solve_two(m) <= p)
		{
			ans=m;
			l=m+1;
		}
		else
			r=m-1;
	}
	return ans;
}
int main()
{
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		cin >> n >> p;
		total=1LL<<n;
		printf("Case #%d: %I64d %I64d\n",cc,one(),two());
	}
	return 0;
}
/*
3
3 4
3 5
3 3

 */
