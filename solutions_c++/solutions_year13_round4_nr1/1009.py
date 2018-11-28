#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <pthread.h>
#define ZERO(X) memset(X,0,sizeof(X))
#define FOR(I,N) for (I=0;I<(N);++I)
#define REV(I,N) for (I=(N)-1;I>=0;--I)
#define FORK(I,K,N) for (I=(K);I<(N);++I)
#define REVK(I,K,N) for (I=(K);I>=0;--I)
#define pb push_back
#define sci(d) scanf("%d",&d)
#define scll(l) scanf("%lld",&l)
#define scull(l) scanf("%llu",&l)
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int test_cases;

inline ull dist (ull n, ull c)
{
	if (c==0) return 0;
	return c*n-c*(c-1)/2;
}

int main ()
{
	int ti;
	cin.sync_with_stdio(false);
	cin>>test_cases;
	FOR(ti,test_cases)
	{
		int n,m,i;
		cin>>n>>m;
		ull op=0,ep=0;
		map< int,pair<int,int> > sub;
		FOR(i,m)
		{
			int o,e,p;
			cin>>o>>e>>p;
			sub[o].first+=p;
			sub[e].second+=p;
			op+=((ull)p*dist(n,e-o))%1000002013;
			op%=1000002013;
		}
		stack< pair<int,int> > st;
		for (map< int,pair<int,int> >::iterator it=sub.begin();it!=sub.end();++it)
		{
			if (it->second.first) st.push(make_pair(it->first,it->second.first));
			int tmp=it->second.second;
			while (tmp)
			{
				pair<int,int> p=st.top();
				st.pop();
				if (tmp>p.second)
				{
					tmp-=p.second;
					ep+=dist(n,it->first-p.first)*p.second;
					ep%=1000002013;
				}
				else
				{
					p.second-=tmp;
					ep+=dist(n,it->first-p.first)*tmp;
					ep%=1000002013;
					tmp=0;
					st.push(p);
				}
			}
		}
		printf("Case #%d: %llu\n",ti+1,(op-ep)%1000002013ULL);
	}
	return 0;
}