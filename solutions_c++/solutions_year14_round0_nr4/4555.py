#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
#define rep(i,n) for(int i=1;i<=n;++i) 
using namespace std;
int n,T;
double a[1020],b[1020];
int ans1,ans2;
int main()
{
//	 freopen("D.in","r",stdin);
//	 freopen("D.out","w",stdout);
	 
	 scanf("%d",&T);
	 
	 rep(ii,T)
	 {
		scanf("%d",&n);
		rep(i,n)scanf("%lf",&a[i]);
		rep(i,n)scanf("%lf",&b[i]);
		sort(a+1,a+1+n);
		sort(b+1,b+1+n);
		int x=n;
		ans1=ans2=0;
		for(int i=n;i>=0;--i)
		{
			if(!x)break;
			while(x>0&&a[i]<b[x])--x;
			if(x)
			{
				++ans1;
				--x;
			}
		}
		x=n;
		for(int i=n;i>=0;--i)
		{
			if(!x)break;
			while(x>0&&b[i]<a[x])--x;
			if(x)
			{
				++ans2;
				--x;
			}
		}
		ans2=n-ans2;
		printf("Case #%d: %d %d\n",ii,ans1,ans2);
	}
	return 0;
}
	
