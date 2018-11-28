#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <memory.h>
#include <cassert>
#include <time.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large(3)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}



long long o[1111],e[1111],p[1111];
long long n,m;
long long md = 1000002013;
long long calc(long long v)
{
	if (v==n) return 0;
	return ((v+1 + n)*(n-v)/2)%md;

}



int main()
{
    init();

	int tst;
	scanf("%d\n",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
		
		scanf("%lld%lld",&n,&m);
		vector <pair < pair <long long, long long> , long long> > arr;


		for (int i=0;i<m;i++)
		{
			scanf("%lld%lld%lld",&o[i],&e[i],&p[i]);
			arr.push_back(make_pair(make_pair(o[i],0),p[i] ));
			arr.push_back(make_pair(make_pair(e[i],1),p[i] ));		
		}
		sort(all(arr));
		long long res=0;
		vector < pair <long long, long long> > ms;
		for (int i = 0 ;i<sz(arr);i++)
		{
			sort(all(ms));
			reverse(all(ms));

			if (i)
			{
				long long d = arr[i].first.first-arr[i-1].first.first;
				for (int j=0;j<sz(ms);j++)
				{
					ms[j].first-=d;
				}
			
			}
			if (arr[i].first.second==0)
			{
				ms.push_back(make_pair(n,arr[i].second) );
			} else
			{
				long long c = arr[i].second;
				for (int j=0; j<sz(ms);j++)
				{
					long long cur = min(c,ms[j].second);
					res+=calc(ms[j].first)*cur;
					res%=md;
					c-=cur;
					ms[j].second-=cur;
					if (c==0) break;
					
				}			
			}	

			while (sz(ms))
			{
				if (ms[0].second==0)
					ms.erase(ms.begin()); else
					break;			
			}

			sort(all(ms));
			reverse(all(ms));
		}
	
		long long res2=0;
		for (int i=0;i<m;i++)
		{
			res2+=calc(n-(e[i]-o[i]))*p[i];
			res2%=md;
		}	
		res2-=res;
		if (res2<0) res2+=md;
		printf("Case #%d: %lld\n",cas,res2);
	}



	

	return 0;
}
