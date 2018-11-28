#include<iostream>
#include<cstdio>
using namespace std;
typedef long long LL;
LL n,p,T,ans1,ans2;

bool check1(LL pos)
{
	LL cnt=0,ret=0;
	for (LL x=pos;x;x=x>>1)
		x--,cnt++;
	for (int i=0;i<cnt;i++)
		ret=ret|(1LL<<n-i-1);
	return ret<p;
}

bool check2(LL pos)
{
	LL cnt=0,ret=(1LL<<n)-1;
	for (LL x=(1LL<<n)-1-pos;x;x=x>>1)
		x--,cnt++;
	for (int i=0;i<cnt;i++)
		ret=ret^(1LL<<n-i-1);
	return ret<p;
}

int main()
{
	cin>>T;
	for (int t=1;t<=T;t++)
	{
		cin>>n>>p;
		LL l=0, r=(1LL<<n)-1;
		while (l<=r)
		{
			LL mid=l+r>>1;
			if (check1(mid)) 
			{
				ans1=mid;
				l=mid+1;
			}
			else 
				r=mid-1;
		}
		l=0, r=(1LL<<n)-1;
		while (l<=r)
		{
			LL mid=l+r>>1;
			if (check2(mid))
			{
				ans2=mid;
				l=mid+1;
			}
			else
				r=mid-1;
		}
		printf("Case #%d: %I64d %I64d\n",t,ans1,ans2);
	}
}