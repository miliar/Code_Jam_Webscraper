#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#define ll double
#define bug puts("here");
#define maxn 20000
#define mm 1000005
#define eps 1e-8
ll c,f,x;
double work(int t)
{
	ll carry=2.0;
	ll res=0;
	for(int i=0;i<t;++i)
	{
		res+=c/carry;
		carry+=f;
	}
	res+=x/carry;
	return res;
}
using namespace std;
int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\B-small-attempt0.in","r",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\B.txt","w",stdout);
	int T,n,m;
	cin>>T;
	for(int kase=1;kase<=T;++kase)
	{
		//cin>>c>>f>>x;
		scanf("%lf%lf%lf",&c,&f,&x);
		int l=0,r=mm;
		int lp,rp;
		ll dl,dr;
		while(l+10<r)
		{
			lp=(2*l+r)/3;
			rp=(l+2*r)/3;
			dl=work(lp);
			dr=work(rp);
			if(dl<dr)
				r=rp;
			else l=lp;
		}
		int ans=l;
		for(int i=l+1;i<=r;++i)
			if(work(i)<work(ans))
				ans=i;
		printf("Case #%d: %.7lf\n",kase,work(ans));
	}
}