#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <sstream>
#define two(x) (1 << (x))
using namespace std;

const int N = 20;

int cntStartKeys, cntChests;
int needKey[N], cntInsideKeys[N];
int insideKeys[N][40];
int startKeys[200];
int f[two(N)];
int T;

void work()
{
	static int ttt = 0;
	printf("Case #%d:", ++ttt);
	scanf("%d%d", &cntStartKeys, &cntChests);
	memset(startKeys, 0, sizeof(startKeys));
	for (int i = 0; i < cntStartKeys; ++i) {
		int x;
		scanf("%d", &x);
		startKeys[x]++;
	}
	for (int i = 0; i < cntChests; ++i) {
		scanf("%d%d", &needKey[i], &cntInsideKeys[i]);
		for (int j = 0; j < cntInsideKeys[i]; ++j)
			scanf("%d", &insideKeys[i][j]);
	}
	int n = cntChests;
	for (int msk = 0; msk < two(n); ++msk) f[msk] = -1;
	f[two(n) - 1] = 0;
	for (int msk = two(n) - 2; msk >= 0; --msk) {
		int keys[200];
		memcpy(keys, startKeys, sizeof(keys));
		for (int i = 0; i < n; ++i) if (msk & two(i)) {
			for (int j = 0; j < cntInsideKeys[i]; ++j) keys[insideKeys[i][j]]++;
			keys[needKey[i]]--;
		}
		for (int nxt = 0; nxt < n; ++nxt) if (!(msk & two(nxt)) && keys[needKey[nxt]] && f[msk | two(nxt)] != -1) {
			f[msk] = nxt;
			break;
		}
	}
	if (f[0] == -1) {
		printf(" IMPOSSIBLE\n");
	} else {
		for (int msk = 0; msk != two(n) - 1; msk |= two(f[msk]))
			printf(" %d", f[msk] + 1);
		printf("\n");
	}
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d\n", &T);
	while (T--) work();
}