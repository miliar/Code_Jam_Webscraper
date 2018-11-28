// Round 1A 2012
// Problem X.

#ifdef _MSC_VER
	#define _CRT_SECURE_NO_WARNINGS
#endif

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
#include <cassert>

using namespace std;

typedef unsigned long long llong;
typedef long double ldouble;
typedef pair<int, int> pint;
typedef pair<double, double> pdouble;
typedef vector<int> vint;
typedef vint::iterator vit;
typedef vector<double> vdouble;
typedef vdouble::iterator vdit;
typedef vector<ldouble> vldouble;
typedef vector<string> vstring;
typedef vector<llong> vllong;
typedef vector<vint> graph;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#ifdef _MSC_VER
	#define VAR(v,i) auto v=(i)
#else
	#define VAR(v,i) __typeof(i) v=(i)
#endif
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

#define ADD_EDGE(g,u,v) g[u].push_back(v),g[v].push_back(u)

#define ST first
#define ND second
#define INF 1000000000
#define INFL 1000000000000000000LL
#define EPS 1e-5
#define MAX 100000

struct Barber
{
	int index;
	llong time, speed;
	
	Barber(int index, llong speed) : index(index), time(0), speed(speed) { }
	
	bool operator< (const Barber& other) const
	{
		return time > other.time || (time == other.time && index > other.index);
	}
};

llong limit(vector<Barber> &V, llong time)
{
	llong out = 0;
	REP(i, SIZE(V))
		out += (time + V[i].speed  - 1) / V[i].speed;
	
	return out;
}

llong bisection(vector<Barber> &V, llong low, llong high, llong N)
{
	while(low + 1 != high)
	{
		llong mid = (low + high) / 2;
		if(limit(V, mid) >= N)
			high = mid;
		else
			low = mid;
	}
	
	return low;
}

int solve()
{
	int B;
	llong N;
	cin >> B >> N;
	
	vector<Barber> V;
	int speed;
	REP(i, B)
		cin >> speed, V.push_back(Barber(i + 1, speed));

	llong time = INFL;
	REP(i, B)
		time = min(time, V[i].speed);
	time = bisection(V, 0, time * N, N);
	
	llong served = limit(V, time);
	N -= served;
	assert(N > 0);

	REP(i, B)
		V[i].time = time % V[i].speed;
	priority_queue<Barber, vector<Barber> > Q;
	REP(i, B)
		Q.push(V[i]);

	REP(i, N - 1)
	{
		Barber next = Q.top();
		Q.pop();
			
		next.time += next.speed;
		Q.push(next);
	}

	return Q.top().index;
}

int main()
{
	int T;
	
	cin >> T;
	REP(t, T)
		printf("Case #%d: %d\n", t + 1, solve());
	
	return 0;
}
