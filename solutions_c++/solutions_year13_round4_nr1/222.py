#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
using namespace std;
const long long MOD = 1000002013;
struct Node
{
	int s, in;
	long long p;
} a[2010];
map<int, long long> mp;
int T, m;
long long n, ans1, ans2;

bool cmp(Node p, Node q)
{
	return p.s < q.s || p.s == q.s && p.in < q.in;
}

long long calc(int o, int e)
{
	long long k = e - o;
	long long tmp1 = k * n % MOD;
	long long tmp2 = k * (k - 1) / 2 % MOD;
	return (tmp1 + MOD - tmp2) % MOD;
}

int main()
{
	int ca = 0;
	scanf("%d", &T);
	while (T--)
	{
		ca++;
		mp.clear();
		scanf("%lld%d", &n, &m);
		ans1 = ans2 = 0;
		for (int i = 1; i <= m; i++)
		{
			int o, e;
			long long p;
			scanf("%d%d%lld", &o, &e, &p);
			a[i * 2 - 1].s = o; a[i * 2 - 1].in = 0; a[i * 2 - 1].p = p;
			a[i * 2].s = e; a[i * 2].in = 1; a[i * 2].p = p;
			ans1 = (ans1 + p * calc(o, e) % MOD) % MOD;
		}
		sort(a + 1, a + 2 * m + 1, cmp);
		for (int i = 1; i <= 2 * m; i++)
			if (a[i].in == 0)
				mp[a[i].s] += a[i].p;
			else
			{
				long long p = a[i].p;
				for (map<int, long long>::reverse_iterator mpi = mp.rbegin(); mpi != mp.rend(); mpi = mp.rbegin())
					if (mpi->second >= p)
					{
						ans2 = (ans2 + p * calc(mpi->first, a[i].s) % MOD) % MOD;
						if (mpi->second > p)
							mpi->second -= p;
						else mp.erase(mpi->first);
						break;
					}
					else
					{
						p -= mpi->second;
						ans2 = (ans2 + (mpi->second) * calc(mpi->first, a[i].s) % MOD) % MOD;
						mp.erase(mpi->first);
					}
			}
		printf("Case #%d: %lld\n", ca, (ans1 - ans2 + MOD) % MOD);
	}
	return 0;
}
