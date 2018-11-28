#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MOD = 1000002013;
const int MAXM = 1000;
struct Journey
{
	int l, r, p;
	int preL, preR;
};
Journey a[MAXM];
int ls[MAXM * 5];
int n, m;

int calcCost(int l, int r)
{
	int len = r - l;
	long long ret = (long long)(n - len + 1 + n) * len / 2;
	return ret % MOD;
}

unsigned long long cnt[MAXM * 5];
int pre[MAXM * 5];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	int totCas;
	scanf("%d", &totCas);
	for (int cas = 1; cas <= totCas; cas++)
	{
		scanf("%d%d", &n, &m);
		int totLs = 0;
		for (int i = 0; i < m; i++)
		{
			scanf("%d%d%d", &a[i].l, &a[i].r, &a[i].p);
			a[i].l--;
			a[i].r--;
			a[i].preL = a[i].l;
			a[i].preR = a[i].r;
			ls[totLs++] = a[i].l * 2;
			ls[totLs++] = a[i].r * 2;
			if (a[i].l > 0)
				ls[totLs++] = a[i].l * 2 - 1;
			if (a[i].r + 1 < n)
				ls[totLs++] = a[i].r * 2 + 1;
		}
		sort(ls, ls + totLs);
		totLs = unique(ls, ls + totLs) - ls;
		for (int i = 0; i < m; i++)
		{
			a[i].l = lower_bound(ls, ls + totLs, a[i].l * 2) - ls;
			a[i].r = lower_bound(ls, ls + totLs, a[i].r * 2) - ls;
			pre[a[i].l] = a[i].preL;
			pre[a[i].r] = a[i].preR;
		}

		long long sum = 0, nowSum = 0;
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < m; i++)
		{
			for (int j = a[i].l; j <= a[i].r; j++)
				cnt[j] += a[i].p;
			sum = (sum + (long long) calcCost(a[i].preL, a[i].preR) * a[i].p % MOD) % MOD;
		}
		while (true)
		{
			bool flag = false;
			for (int i = 0; i < totLs; i++)
				if (cnt[i] > 0)
				{
					unsigned long long minVal = cnt[i];
					int nxt = i;
					for (; cnt[nxt] > 0 && nxt < totLs; nxt++)
						minVal = min(minVal, cnt[nxt]);
					unsigned long long tmp = minVal;
					minVal %= MOD;
					nxt--;
					nowSum = (nowSum + (long long)calcCost(pre[i], pre[nxt]) * minVal % MOD) % MOD;
					for (int j = i; j <= nxt; j++)
					{
						cnt[j] -= tmp;
					}
					flag = true;
					break;
				}
			if (flag == false)	break;
		}
		int ans = (sum - nowSum + MOD) % MOD;
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
