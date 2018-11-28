#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;
const int inf=~0U>>2;
int tt,ll,rr,tot;
double r,t,k,ans;
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&tt);
	for(int o=1;o<=tt;++o)
	{
		scanf("%lf%lf",&r,&t);
		k=2*r+1;
		ll=1;rr=inf;
		tot=0;
		while (ll<=rr)
		{
			double mid=(ll+rr)/2;
			ans=mid*(k-2)+2*mid*mid;
			if (ans<=t) tot=mid,ll=mid+1;else rr=mid-1;
		}
		printf("Case #%d: %d\n",o,tot);
	}
}