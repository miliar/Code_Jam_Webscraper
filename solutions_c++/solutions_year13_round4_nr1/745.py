#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

#define CY 1005
typedef long long LL;
#define INF 0x3f3f3f3f3f3f3f3fLL

const int mod = 1000002013;

struct P {
	int fro, to, p;
	bool operator < (const P &rhs) const { 
		return fro ^ rhs.fro ? fro < rhs.fro : to < rhs.to;
	}
}ar[CY];

int tb[CY << 1];
LL rec[CY << 1];
int N, M, idx;
LL pre;

void input(int n, int m) {
	idx = 0;
	pre = 0;
	for (int i = 0; i < m; ++i) {
		scanf("%d%d%d", &ar[i].fro, &ar[i].to, &ar[i].p);
		LL num = ar[i].to - ar[i].fro;
		pre += ar[i].p * ((2 * n - 1 - num) * num / 2 % mod) % mod;
		tb[idx++] = ar[i].fro;
		tb[idx++] = ar[i].to;
	}
	sort(ar, ar + m);
	sort(tb, tb + idx);
	idx = unique(tb, tb + idx) - tb;
}

int F(int value) {
	int lt = 0, rt = idx - 1, mid;
	while (lt <= rt) {
		mid = (lt + rt) >> 1;
		if (tb[mid] == value) return mid;
		else if (tb[mid] > value) rt = ~-mid;
		else lt = -~mid;
	}
	while (true);
}

void solve(int n, int m) {
	for (int i = 0; i < m; ++i) {
		ar[i].fro = F(ar[i].fro);
		ar[i].to = F(ar[i].to);
	}
	for (int i = 0; i < m; ++i) {
		for (int j = ar[i].fro; j < ar[i].to; ++j) {
			rec[j] += ar[i].p;
		}
	}
	LL sum = 0, ans;
	int fro = 0;
	while (fro < idx) {
		int i;
		ans = INF;
		for (i = fro; i < idx; ++i) {
			if (rec[i] > 0) ans = min(ans, rec[i]);
			else break;
		}
		LL num = (tb[i] - tb[fro]);
		sum += ans * ((2 * n - 1 - num) * num / 2 % mod) % mod;
		sum %= mod;
		for (int j = fro; j < i; ++j) {
			rec[j] -= ans;
		}
		for ( ; !rec[fro]; ++fro);
	}
//	printf("%lld\n", sum);
	int res = (int)((pre - sum)% mod + mod) % mod;
	printf("%d\n", res);
}

int main(void) {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int Cas = 1; Cas <= cas; ++Cas) {
		scanf("%d%d", &N, &M);
		input(N, M);
		printf("Case #%d: ", Cas);
		solve(N, M);
	}
	return 0;
}
