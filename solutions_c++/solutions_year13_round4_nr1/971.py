#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;

LL MOD = 1000002013;

LL min(LL a, LL b) {return a < b ? a : b;}

struct Node
{
	LL station, p;
};

bool operator<(const Node &a, const Node &b)
{
	if (a.station == b.station) return a.p < b.p;
	return a.station < b.station;
}

int T;
LL N, M, e, o, p;
Node a[2005];
Node b[50000];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cin >> N >> M;
		memset(a, 0, sizeof(a));
		LL cost1 = 0;
		for(int i = 0; i < M; i++)
		{
			cin >> e >> o >> p;
			LL d = o - e;
			cost1 = (cost1 + ((N * d) % MOD - d * (d - 1) / 2) * p % MOD) % MOD;
			Node cur1;
			cur1.station = e;
			cur1.p = -p;
			Node cur2;
			cur2.station = o;
			cur2.p = p;
			a[i * 2] = cur1;
			a[i * 2 + 1] = cur2;
		}
		sort(a, a + (2 * M));
		LL cost2 = 0;
		int s = 0;
		for(int i = 0; i < M * 2; i++)
		{
			if (a[i].p == 0) continue;
			if (a[i].p < 0)
			{
				if (s == 0 || b[s - 1].station != a[i].station)
				{
					s++;
					b[s].station = a[i].station;
					b[s].p = -a[i].p;
				}
				else b[s].p -= a[i].p;
			}
			else
			{
				while (a[i].p)
				{
					if (a[i].p >= b[s].p)
					{
						LL d = a[i].station - b[s].station;
						if (d > 0)
							cost2 = (cost2 + ((N * d) % MOD - d * (d - 1) / 2) * b[s].p % MOD) % MOD;
						a[i].p -= b[s].p;
						b[s].p = 0;
						s--;
					}
					else
					{
						LL d = a[i].station - b[s].station;
						if (d > 0)
							cost2 = (cost2 + ((N * d) % MOD - d * (d - 1) / 2) * a[i].p % MOD) % MOD;
						b[s].p -= a[i].p;
						a[i].p = 0;
					}
				}
			}
		}
		//cout << cost1 << " " << cost2 << endl;
		LL ans = ((cost1 - cost2) % MOD + MOD) % MOD;
		printf("Case #%d: ", t);
		cout << ans << endl;
	}
	return 0;
}
