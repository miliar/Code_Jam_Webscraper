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
using namespace std;
int ans1,ans2;
set<double> a,b,c;
set<double>::iterator ita,itb;
int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\D-large.in","r",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\D.txt","w",stdout);
	int T,n,m;
	cin>>T;
	for(int kase=1;kase<=T;++kase)
	{
		scanf("%d",&n);
		a.clear();
		b.clear();
		c.clear();
		double d;
		for(int i=0;i<n;++i)
			scanf("%lf",&d),a.insert(d);
		for(int i=0;i<n;++i)
			scanf("%lf",&d),b.insert(d),c.insert(d);
		ans1=ans2=0;
		for(ita=a.begin();ita!=a.end();ita++)
		{
			d=*ita;
			itb=upper_bound(b.begin(),b.end(),d);
			if(itb==b.end())
				ans2++;
			else b.erase(itb);
		}
		for(ita=a.begin();ita!=a.end();++ita)
		{
			if(*ita>*c.begin())
				ans1++,c.erase(c.begin());
		}
		printf("Case #%d: %d %d\n",kase,ans1,ans2);
	}
}