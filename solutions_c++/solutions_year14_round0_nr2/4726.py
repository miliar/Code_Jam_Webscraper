#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
#define rep(i,n) for(int i=1;i<=n;++i)
using namespace std;
int lft,rgt,mid,T,ans;
double X,C,F;
const double eps=1e-8;
bool getpd(int n)
{
	double x1=X-C;
	double y1=2.0+F*n;
	double x2=X;
	double y2=2.0+F*(n+1);
	return (x1/y1)<=(x2/y2+eps);
}
double get_ans(int n)
{
	double x=0;
	rep(i,n)x+=C/(2+F*(i-1));
	x+=X/(2+n*F);
	return x;
}
int main()
{
//	freopen("B.in","r",stdin);
//	freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	rep(ii,T)
	{
		lft=0;
		rgt=1;
		scanf("%lf%lf%lf",&C,&F,&X);
		while(!getpd(rgt))rgt=rgt*2;
		while(lft<=rgt)
		{
			int mid=(lft+rgt)>>1;
			if(getpd(mid))
			{
	 			ans=mid;
	 			rgt=mid-1;
			}else lft=mid+1;
		}
		printf("Case #%d: %.7lf\n",ii,get_ans(ans));
	}
	return 0;
}