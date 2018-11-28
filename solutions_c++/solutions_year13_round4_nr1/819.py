/* by Ashar Fuadi (fushar) */

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>

#include <vector>
#include <queue>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0, _n = (int)n; i < _n; i++)
#define FOR(i,a,b) for (int i = (int)a, _b = (int)b; i <= _b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

const ll MOD = 1000002013;

#define pb push_back
#define mp make_pair

struct event
{
	ll x;
	ll p;
	int type;
	int id;

	bool operator<(const event& that) const
	{
		if (x == that.x)
			return type < that.type;
		return x < that.x;
	}
};


int T, M;
ll N;
event E[2005];

int order[2005];
ll X[2005];
ll P[2005];

int main()
{
	cin >> T;
	REP(tc, T)
	{
		cin >> N >> M;

		ll total = 0;
		REP(i, M)
		{
			ll o, e, p;
			cin >> o >> e >> p;
			X[i] = o;

			ll n = e - o;
			ll a = N;
			ll Un = N - n + 1;
			ll ow = n * (a + Un) / 2;
			ow %= MOD;
			ow *= (p % MOD);
			ow %= MOD;

			total += ow;
			total %= MOD;

			E[2*i] = (event){o, p, 0, i};
			E[2*i+1] = (event){e, p, 1, i};
		}

		sort(E, E+2*M);
		REP(i, M)
			P[i] = 0;

		int num = 0;
		REP(i, 2*M) if (E[i].type == 0)
			order[num++] = E[i].id;

		assert(num == M);

		ll res = 0;
		REP(i, 2*M)
		{
			if (E[i].type == 0)
				P[E[i].id] = E[i].p;
			else
			{
				ll p = E[i].p;
				for (int j = M-1; j >= 0; j--)
				{
					int m = order[j];
					ll pp = min(p, P[m]);
					p -= pp;
					P[m] -= pp;


					ll n = E[i].x - X[m];
					ll a = N;
					ll Un = N - n + 1;
					ll ow = n * (a + Un) / 2;
					ow %= MOD;
					ow *= (pp % MOD);
					ow %= MOD;
					res += ow;
					res %= MOD;
				}
				assert(p == 0);
			}
		}
		cout << "Case #" << (tc+1) << ": " << (total - res + MOD) % MOD << endl;
	}
}