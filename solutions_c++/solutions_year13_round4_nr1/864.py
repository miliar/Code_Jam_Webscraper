#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

typedef long long llong;
typedef long double ldouble;
typedef pair<int, int> pint;
typedef pair<double, double> pdouble;
typedef vector<int> vint;
typedef vector<double> vdouble;
typedef vector<llong> vllong;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

#define ST first
#define ND second
#define INF 1000000000
#define INFL 1000000000000000000LL
#define EPS 1e-5
#define MAXVAL 1000002013

struct route
{
	int start, finish;
	llong people;
};

llong calculate(int start, int finish, int N)
{
	llong k = finish - start;
	return k * (N + 1) - k * (k + 1) / 2;
}

int main()
{
	int T, N, M;
	
	cin >> T;
	REP(t, T)
	{
		cin >> N >> M;
		
		map<int, int, greater<int> > start, finish, current;
		llong gain = 0, loss = 0;
		REP(i, M)
		{
			int s, f, p;
			cin >> s >> f >> p;
			gain += ((calculate(s, f, N) % MAXVAL) * p) % MAXVAL, gain %= MAXVAL;
			
			start[s] += p, finish[f] += p;
		}
		
		REP(i, N)
		{
			
			if(start.find(i + 1) != start.end())
				current[i + 1] += start[i + 1];
			if(finish.find(i + 1) == finish.end())
				continue;

			int &out = finish[i + 1];
			while(out)
			{
				map<int, int, greater<int> >::iterator it = current.begin();
				int people = min(out, it->second);
				loss += ((calculate(it->first, i + 1, N) % MAXVAL) * people) % MAXVAL, loss %= MAXVAL;
				
				it->second -= people, out -= people;
				if(it->second == 0)
					current.erase(it);
			}
		}
		printf("Case #%d: %lld\n", t + 1, gain >= loss ? gain - loss : gain + MAXVAL - loss);
	}
	
	return 0;
}