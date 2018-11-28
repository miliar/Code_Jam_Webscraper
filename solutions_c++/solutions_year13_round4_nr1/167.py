#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cstdio>
#include <ctime>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <cassert>
#include <iostream>
#include <cmath>
#include <sstream>
#include <complex>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long int64;
typedef unsigned long long uint64;

#define y1 _dsfkjdsfksdj
#define y0 _sfsdkfdop

typedef unsigned uint;
typedef vector<int64> vi64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<int64,int64> pii64;
typedef pair<pii,int> piii;
typedef pair<pii,pii> piiii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<double,int> pdi;
typedef pair<double,double> pdd;

typedef pair<int,int64> spii;

struct ride
{
	int L;
	int R;
	int C;

	void read()
	{
		scanf("%d%d%d", &L, &R, &C);
	}

	bool operator < (const ride &B) const
	{
		return pii(L, R) < pii(B.L, B.R);
	}
};

int nt;
int n, m;
int l;
ride rides[1 << 10];
pii ev[1 << 11];
priority_queue <spii> q;

const int64 toMod = 1000002013;

inline void init()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; ++i)
		rides[i].read();
}

inline int64 get_length(int64 L)
{
	return (int64)(n * L - (L * (L - 1)) / 2) % toMod;
}

inline int64 solve()
{
	sort(rides, rides + m);
	l = 0;
	int64 res = 0;
	for (int i = 0; i < m; ++i)
	{
		res += get_length(rides[i].R - rides[i].L) * (int64)rides[i].C;
		res %= toMod;
		ev[l++] = pii(rides[i].L, -rides[i].C);
		ev[l++] = pii(rides[i].R, rides[i].C);
	}
	sort(ev, ev + l);
	int i = 0;
	while (i < l)
	{
		int j = i + 1;
		while (j < l && ev[j].first == ev[i].first) ++j;
		int was = 0;
		int64 curcnt = 0;
		for (int t = i; t < j; ++t)
		{
			if (ev[t].second < 0)
			{
				curcnt -= (int64)ev[t].second;
			} else {
				if (!was && curcnt)
				{
					q.push(spii(ev[t].first, curcnt));
					was = 1;
				}
				int64 now = ev[t].second;
				while (now)
				{
					spii cur = q.top();
					q.pop();
					int64 dif = min(cur.second, now);
					now -= dif;
					cur.second -= dif;
					if (cur.second)
						q.push(cur);
					dif %= toMod;
					res -= ((get_length(ev[t].first - cur.first) * dif) % toMod);
					while (res < 0) res += toMod;
				}
			}
		}
		if (!was && curcnt)
		{
			q.push(spii(ev[i].first, curcnt));
			was = 1;
		}
		i = j;
	}
	return res;
}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		init();
		int64 res = solve();
		cout << "Case #" << tn << ": " << res << endl;
	}

    return 0;
}