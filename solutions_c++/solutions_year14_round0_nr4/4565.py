#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define EPS 1e-8
#define MAXN 1005
#define MAXE 1005

typedef pair<int, int> pii;
typedef long long ll;

int T, N;
double naomi[MAXN], ken[MAXN];

int ScoreOfDeceitfulWar() {
	int r = 0, j = 0;
	for (int i = 0; i < N; ++i) {
		if (naomi[i] > ken[j]) {
			r++, j++;
		}
	}
	return r;
}

int ChosenByKen(double x, bool *b) {
	int ix = upper_bound(ken, ken + N, x) - ken;
	if (ix == N) {
		for (int i = 0; i < N; ++i) {
			if (b[i] == false) {
				b[i] = true; return i;
			}
		}
	}
	for (int i = ix; i < N; ++i) {
		if (b[i] == false) {
			b[i] = true; return i;
		}
	}
	for (int i = 0; i < N; ++i) {
		if (b[i] == false) {
			b[i] = true; return i;
		}
	}
	return -1;
}

int ScoreOfWar() {
	static bool used[MAXN];
	memset(used, false, sizeof(used));

	int r = 0;
	for (int i = N - 2; i >= 0; i -= 2) {
		int j = ChosenByKen(naomi[i], used);
		if (naomi[i] > ken[j]) r++; 
	}
	for (int i = N - 1; i >= 0; i -= 2) {
		int j = ChosenByKen(naomi[i], used);
		if (naomi[i] > ken[j]) r++; 
	}
	return r;
}

int main() {
	scanf("%d", &T);
	for (int nCase = 1; nCase <= T; ++nCase) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%lf", naomi + i);
		}
		for (int i = 0; i < N; ++i) {
			scanf("%lf", ken + i);
		}
		sort(naomi, naomi + N);
		sort(ken, ken + N);

		int y = ScoreOfDeceitfulWar();
		int z = ScoreOfWar();
		printf("Case #%d: %d %d\n", nCase, y, z);
	}
	return 0;
}


