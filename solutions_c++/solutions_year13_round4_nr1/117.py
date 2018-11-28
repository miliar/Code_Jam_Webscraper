#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

typedef long long ll;
const ll MOD=1000002013;

ll cost(ll n, ll len)
{
	n%=MOD;
	len%=MOD;
	return ((len*n%MOD-len*(len+1)/2%MOD)%MOD+MOD)%MOD;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		int n,m;
		ll res1=0,res2=0;
		scanf("%d%d",&n,&m);
		map<int,vector<pair<int,ll> > > to;
		map<int,vector<pair<int,ll> > >::iterator it;
		while(m--)
		{
			int s,e,c;
			scanf("%d%d%d",&s,&e,&c);
			to[s].push_back(make_pair(e,c));
			to[e];
			res1=(res1+cost(n,e-s)*c%MOD)%MOD;
		}
		for(typeof to.begin() i=to.begin();i!=to.end();i++)
			sort(i->second.begin(),i->second.end());
		priority_queue<pair<int,ll> , vector<pair<int,ll> >, greater<pair<int,ll> > > q;
		map<int,ll> entry_ticket;
		it=to.begin();

		while(it!=to.end())
		{
			ll leavecnt=0;
			for(int i=0;i<it->second.size();i++)
			{
				q.push(it->second[i]);
				entry_ticket[it->first]+=it->second[i].second;
			}
			while(!q.empty() && q.top().first==it->first)
			{
				leavecnt+=q.top().second;
				q.pop();
			}
			map<int,ll>::reverse_iterator jt=entry_ticket.rbegin();
			for(;leavecnt;)
			{
				ll v=min(leavecnt,jt->second);
				jt->second-=v;
				leavecnt-=v;
				res2=(res2+cost(n,it->first-jt->first)*v%MOD)%MOD;
				if(!jt->second)
				{
					int entry=jt->first;
					jt++;
					entry_ticket.erase(entry);
				}
				else
					jt++;
			}
			it++;
		}
		printf("Case #%d: %lld\n",test,((res1-res2)%MOD+MOD)%MOD);
	}
	return 0;
}
