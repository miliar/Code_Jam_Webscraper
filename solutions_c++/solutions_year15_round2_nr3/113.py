#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int magic = 12;
const int nmax = 1005;

struct Hiker
{
	double startTime, endTime;
};

struct EndTime
{
	double endTime;
	EndTime(double _endTime)
	{
		endTime = _endTime;
	}
	bool operator < (const EndTime &oth) const
	{
		return endTime < oth.endTime - eps;
	}
	bool operator == (const EndTime &oth) const
	{
		return fabs(endTime - oth.endTime) < eps;
	}
};

int n;
int D[nmax], H[nmax], M[nmax];
vector < Hiker > hikers;
vector < EndTime > endTimes;

void read()
{
	hikers.clear();
	endTimes.clear();

	scanf("%d", &n);
	for (int i = 0; i < n; i ++)
		scanf("%d%d%d", &D[i], &H[i], &M[i]);
}

void addHiker(Hiker h)
{
	hikers.pb(h);
	endTimes.pb(h.endTime);
}

void addHiker(int start, int timePerLap)
{
	double v = 360.0 / timePerLap, period;

	Hiker h;
	h.startTime = - start / v;
	h.endTime = (360.0 - start) / v;
	addHiker(h);

	for (int i = 1; i < magic; i ++)
	{
		h.startTime += timePerLap;
		h.endTime += timePerLap;
		addHiker(h);
	}
}

int calc(double endTime)
{
	int ret = 0;
	for (int i = 0; i < sz(hikers); i ++)
	{
		if (hikers[i].startTime < 0.0 && hikers[i].endTime > endTime ||
			hikers[i].startTime > 0.0 && hikers[i].endTime < endTime)
		{
			ret++;
		}
	}
	return ret;
}

bool solve()
{
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < H[i]; j ++)
		{
			addHiker(D[i], M[i] + j);
		}
	}
	endTimes.pb(0.0);
	endTimes.pb(2 * INF);
	sort(all(endTimes));
	endTimes.erase(unique(all(endTimes)), endTimes.end());
	
	int ans = sz(hikers);
	for (int i = 0; i < sz(endTimes) - 1; i ++)
	{
		double mid = (endTimes[i].endTime + endTimes[i + 1].endTime) / 2.0;
		ans = min(ans, calc(mid));
	}
	printf("%d\n", ans);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
