#include <iostream>
#include <string.h>
#include <stdio.h>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <math.h>

using namespace std;
long long  p,q;
long long ans,tem,t;
long long gcd(long long a,long long b)
{
	if (a%b==0) return b;
	else return gcd(b,a%b);
}
void work()
{
	scanf("%ld/%ld",&p,&q);
	ans=0;
	if (p==0||q==0)
	{
		ans=-1;
		return ;
	}
	if	(p==1&&q==1)
	{
		ans=0;
		return ;
	}
	if (p>q)
	{
		ans=-1;
		return ;
	}
	tem=gcd(q,p);
	p=p/tem;
	q=q/tem;
	if (q%2==1)
	{
		ans=-1;
		return ;
	}
	t=q;
	while (t%2==0)
	{
		t/=2;
	}
	if (t!=1)
	{
		ans=-1;
		return ;
	}
	ans=0;
	while (true)
	{	
		if (p>=q) break;
		p*=2;
		ans++;
	}
}
int main()
{
	int T;
	int cas;
	cas=0;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>T;
	while (T--)
	{
		work();
		cas++;
		if (ans!=-1)
			cout<<"Case #"<<cas<<": "<<ans<<endl;
		else
			cout<<"Case #"<<cas<<": "<<"impossible"<<endl;;
	}
	return 0;
}
