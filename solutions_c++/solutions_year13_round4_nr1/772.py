#include <stdio.h>
#include <string.h>
#include <map>
#include <algorithm>
#define MIN(a, b)    ((a) < (b) ? (a) : (b))
#define MOD 1000002013
using namespace std;

int n, m, real_n;

struct info
{
	int st, ed, pe;
};

info record[2000];
int arr[5000];
map<int, int> mp;
int uhash[2000];

long long stp[2000], edp[2000];

long long reduce, original, tmp;

void Normalize()
{
	int i;
	memset (uhash, 0, sizeof uhash);
	mp = map<int, int>();
	for (i = 0; i < m; i++)
	{
		arr[2 * i] = record[i].st;
		arr[2 * i + 1] = record[i].ed;
	}
	sort (arr, arr + 2 * m);
	int cnt = 0;
	mp[arr[0]] = 0;
	uhash[0] = arr[0];
	for (i = 1; i < 2 * m; i++)
	{
		if (arr[i] != arr[i - 1])
		{
			cnt++;
			mp[arr[i]] = cnt;
			uhash[cnt] = arr[i];
		}
	}
	for (i = 0; i < m; i++)
	{
		record[i].st = mp[record[i].st];
		record[i].ed = mp[record[i].ed];
		// printf("%d %d\n", record[i].st, record[i].ed);
	}
	real_n = n;
	n = cnt + 1;
}

long long Fast(long long tmp, long long tms)
{
	long long cube = tmp;
	long long ret = 0;
	while (tms)
	{
		if (tms % 2 == 1)
		{
			ret += cube;
			ret %= MOD;
		}
		cube += cube;
		cube %= MOD;
		tms /= 2;
	}
	return ret;
}

void Work()
{
	// printf("n = %d\n", n);
	memset (stp, 0, sizeof stp);
	memset (edp, 0, sizeof edp);
	int i, j, pos;
	long long tp;
	int dist;
	for (i = 0; i < m; i++)
	{
		pos = record[i].st;
		stp[pos] += record[i].pe;
		pos = record[i].ed;
		edp[pos] += record[i].pe;
	}
	// for (i = 0; i < n; i++)
		// printf("%I64d %I64d\n", stp[i], edp[i]);
	for (i = n - 1; i >= 0; i--)
	{
		for (j = i; j < n; j++)
		{
			if (stp[i] == 0)
				break;
			if (edp[j] == 0)
				continue;
			dist = uhash[j] - uhash[i];
			// printf("i = %d j = %d   ui = %d uj = %d dist = %d\n", i, j, uhash[i], uhash[j], dist);
			tmp = 1ll * (real_n + (real_n - dist + 1)) * dist / 2;
			tmp %= MOD;
			tp = MIN(stp[i], edp[j]);
			// printf("tp = %I64d\n", tp);
			tmp = Fast(tmp, tp);
			//tmp = (tmp * tp) % MOD;
			// printf("tmp = %I64d\n", tmp);
			reduce += tmp;
			reduce %= MOD;
			// printf("match at: %d %d %I64d    %I64d\n", i, j, tp, reduce);
			stp[i] -= tp;
			edp[j] -= tp;
		}
	}
}

int main()
{
	int cas, t;
	int i, j;
	long long ret;
	int s, e, p;
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++)
	{
		original = reduce = 0;
		scanf("%d%d", &n, &m);
		for (i = 0; i < m; i++)
		{
			scanf("%d%d%d", &s, &e, &p);
			tmp = 1ll * (n + (n - (e - s) + 1)) * (e - s) / 2;
			tmp %= MOD;
			tmp = (tmp * p) % MOD;
			original += tmp;
			original %= MOD;
			record[i].st = s;
			record[i].ed = e;
			record[i].pe = p;
			// printf("Original: %d\n", original);
		}
		Normalize();
		Work();
		ret = ((original - reduce) % MOD + MOD) % MOD;
		printf("Case #%d: %I64d\n", cas, ret);
	}
	return 0;
}




