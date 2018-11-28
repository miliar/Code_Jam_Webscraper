#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <iomanip>
#define MOD 1000002013
using namespace std;
struct st
{
	int st;
	int fl;
	long long v;
}a[5001] = {0};
bool operator < (const st &x, const st &y)
{
	if (x.st < y.st)
		return true;
	else if (x.st == y.st && x.fl == 1)
		return true;
	else
		return false;
}
int q[10001] = {0};
int ql = 0;
int n, m;
long long getans(long stx, long enx)
{
	long long N = enx - stx;
	return ((long long)(n + n - N) * (N + 1)  / 2) % MOD; 
}
int main()
{
	int tot, tt;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &tot);
	for (int tt = 1; tt <= tot; tt++)
	{


		cin >> n >> m;
		int al = 0;
		long long used = 0;
		for (int i = 1; i <= m; i++)
		{
			int stx, enx, usp;
			cin >> stx >> enx >> usp;
			al++;
			a[al].st = stx;
			a[al].fl = 1;
			a[al].v = usp;
			al++;
			a[al].st = enx;
			a[al].fl = -1;
			a[al].v = usp;
			used += (usp * getans(stx, enx)) % MOD;
			used %= MOD;
		}
		sort(a + 1, a + al + 1);
		long long ans = 0;
		for (int i = 1; i <= al; i++)
		{
			if (a[i].fl == 1)
			{
				ql++;
				q[ql] = i;
			} else
			{
				while (ql && a[i].v)
				{
					int t = q[ql];
					if (a[t].v <= a[i].v)
					{
						a[i].v -= a[t].v;
						ans += (a[t].v * getans(a[t].st, a[i].st)) % MOD;
						ans %= MOD;
						a[t].v = 0;	
					} else
					{
						a[t].v -= a[i].v;
						ans += (a[i].v * getans(a[t].st, a[i].st)) % MOD;
						ans %= MOD;
						a[i].v = 0;
						break;
					}
					ql--;
				}
			}
		}
		long long tmp;
		tmp = ans;
		ans = used;
		used = tmp;
		ans -= used;
		ans = (ans + MOD) % MOD;
		cout << "Case #" << tt << ": ", tt;
		cout << ans << endl;
	}
	return 0;
}
