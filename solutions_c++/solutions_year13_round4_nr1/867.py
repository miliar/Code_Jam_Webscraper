#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <set>
#include <map>

using namespace std;

long long p = 1000002013;
long long n,m;
long long dist(long long a,long long b)
{
	if (a==b)
		return 0;
	long long s = abs(a - b + .0);
	s = n - s;
	return ((n*(n+1)/2 -1) - (s*(s+1)/2-1))%p;
}
int main()
{	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int testcnt;
	cin>>testcnt;
	for (int curtest = 1; curtest<=testcnt;curtest++)
	{
		cout<<"Case #"<<curtest<<": ";
		
		cin>>n>>m;
		map<long long ,pair<long,long> > mp;
		stack<pair<long long, long long > > entr;
		long long res1 = 0;
		for (int i=0;i<m;i++)
		{
			long long o,e,l;
			cin>>o>>e>>l;
			if (mp.count(o))
			{
				mp[o].first+=l;
			}
			else
			{
				mp[o] = make_pair(l,0);
			}
			if (mp.count(e))
			{
				mp[e].second+=l;
			}
			else
			{
				mp[e] = make_pair(0,l);
			}
			res1 = (res1 + (l * dist(o, e)) % p ) % p;
		}
		long long res2 = 0;
		for (map<long long ,pair<long,long> >::iterator it  = mp.begin();
			it!=mp.end();
			it++)
		{
			if (it->second.first)
			{
				entr.push(make_pair(it->first, it->second.first));
			}
			if (it->second.second)
			{
				long long cur = it->first;
				long long need = it->second.second;
				while (need)
				{
					long long a = entr.top().first;
					long long b = entr.top().second;
					long long c = min(b, need);

					res2 = (res2 + (c * dist(a, cur))%p) % p;
					need -=c;
					entr.top().second -=c;
					if (c == b)
						entr.pop();
				}
			}
		}
		long long res = res1 - res2 ;
		if (res<0)
			res+=p;
		cout<<res;
		cout<<"\n";
	}
	return 0;
}
