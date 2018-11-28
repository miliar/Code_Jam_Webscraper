/*
 * program: google code jam 2013 round 2. a
 * writer: 67h2gak
 * date: 2013.6.1
*/
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int MAXM = 2001, MOD = 1000002013;

struct Pair{
	int x, y, c;
} a[MAXM], tmp[MAXM * MAXM];

LL cnt[MAXM][MAXM];
int key[MAXM], ks;
int n, m, ans, ans0;

int cost(int len)
{
	return (((LL)n + n - len + 1) * len / 2) % MOD;
}

void init()
{
	scanf("%d%d", &n, &m); ans0 = 0; ks = 0;
	for (int i = 0; i < m; i ++){
		scanf("%d%d%d", &a[i].x, &a[i].y, &a[i].c);
		key[ks ++] = a[i].x; key[ks ++] = a[i].y;
		ans0 += (LL)cost(a[i].y - a[i].x) * a[i].c % MOD;
		ans0 %= MOD;
	}
}

bool cmp(Pair a, Pair b)
{
	return a.x < b.x || (a.x == b.x && a.y > b.y);
}

bool cmp2(Pair a, Pair b)
{
	return a.c < b.c;
}

void work()
{
	memset(cnt, 0, sizeof(cnt));
	sort(key, key + ks); ks = unique(key, key + ks) - key;
	sort(a, a + m, cmp);
	for (int i = 0; i < m; i ++){
		a[i].x = lower_bound(key, key + ks, a[i].x) - key;
		a[i].y = lower_bound(key, key + ks, a[i].y) - key;
		cnt[a[i].x][a[i].y] += a[i].c;
	}
	for (int i = 1; i < ks; i ++){
		int k = i, l;
		for (int j = 0; j < i; j ++) if (cnt[j][i]){
			LL &d = cnt[j][i];
			for (k = i; k >= j && d; k --)
				for (l = i+1; l < ks && d; l ++) if (cnt[k][l]){
					int x = d; if (cnt[k][l] < x) x = cnt[k][l];
					cnt[k][l] -= x; d -= x;
					cnt[j][l] += x; cnt[k][i] += x;
					if (!d){k ++;}
				}
		}
	}
	ans = 0;
	for (int i = 0; i < ks; i ++)
		for (int j = i; j < ks; j ++){
			ans += cost(key[j] - key[i]) * (LL)cnt[i][j] % MOD;
			ans %= MOD;
		}
}

void print()
{
	printf("%d\n", ((ans0 - ans) % MOD + MOD) % MOD);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t ++){
		init();
		work();
		printf("Case #%d: ", t);
		print();
	}
	return 0;
}
