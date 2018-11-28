#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define LL long long

struct node
{
	LL s,v;
	node () {s=v=0;}
	node (LL ss,LL vv) {s=ss;v=vv;}
	bool operator < (node b) const
	{
		return v<b.v;
	}
};

int T;
LL e,r,n;
LL v[16384];
multiset <node> q;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int ww=1;ww<=T;ww++)
	{
		printf("Case #%d: ",ww);
		scanf("%I64d%I64d%I64d",&e,&r,&n);
		r=min(e,r);
		for (int i=1;i<=n;i++)
			scanf("%I64d",v+i);
		q.clear();
		q.insert(node(e,0));
		LL ans=0;
		for (int i=1;i<=n;i++)
		{
			LL ns=0;
			while (!q.size()==0)
			{
				node tmp=*q.begin();
				if (tmp.v>=v[i]) break;
				ans+=(v[i]-tmp.v)*tmp.s;
				ns+=tmp.s;
				q.erase(q.begin());
			}
			if (ns!=0) q.insert(node(ns,v[i]));
			LL ws=0;
			while (ws<r)
			{
				multiset <node> :: iterator xx=q.end();
				xx--;
				node tmp=*(xx);
				LL tv=tmp.v;
				LL ts=tmp.s;
				if (ts+ws<=r)
				{
					ws+=ts;
					q.erase(xx);
				}
				else
				{
					q.erase(xx);
					q.insert(node(ts+ws-r,tv));
					ws=r;
				}
			}
			q.insert(node(ws,0));
		}
		printf("%I64d\n",ans);
	}
    return 0;
}
