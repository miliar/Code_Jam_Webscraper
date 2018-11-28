
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <ctime>
#include <cstring>
#include <deque>
#include <queue>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
#define MAXN 1020
//-----------------------------------------------------------
int N, n[MAXN];
int e[MAXN];
// check availability
bool check1(int c) {
	int tmpe[MAXN];
	int tmpn[MAXN];
	memcpy(tmpe, e, sizeof(e));
	memcpy(tmpn, n, sizeof(n));
	tmpn[c] -= 1;
	for (int k = 0; k < N; k++) {
//		if (k == c) tmpe[k] -= 1;
		if (k != c) {
			tmpe[k] -= 1;
		}
//		printf("%d => tmpn[%d] = %d, tmpe[%d] = %d <===\n", c, k, tmpn[k], k, tmpe[k]);
	}
	for (int k = 0; k < N; k++) {
//		printf("%d => tmpn[%d] = %d, tmpe[%d] = %d\n", c, k, tmpn[k], k, tmpe[k]);
		if (tmpn[k] > tmpe[k]) {
//			printf("false\n");
			return false;
		}
	}
	printf(" %c", 'A' + c);
	memcpy(e, tmpe, sizeof(e));
	memcpy(n, tmpn, sizeof(n));
	return true;
}

bool check2(int a, int b) {
	int tmpe[MAXN];
	int tmpn[MAXN];
	memcpy(tmpe, e, sizeof(e));
	memcpy(tmpn, n, sizeof(n));
	tmpn[a] -= 1;
	tmpn[b] -= 1;
	// check availability
	for (int k = 0; k < N; k++) {
		if (k == a) tmpe[k] -= 1;
		if (k == b) tmpe[k] -= 1;
		if (k != a && k != b) {
			tmpe[k] -= 2;
		}
	}
	for (int k = 0; k < N; k++) {
		if (tmpn[k] > tmpe[k]) {
			return false;
		}
	}
	printf(" %c%c", 'A' + a, 'A' + b);
	memcpy(e, tmpe, sizeof(e));
	memcpy(n, tmpn, sizeof(n));
	return true;
}
bool rem() {
	for (int i = 0; i < N; i++) {
		if (n[i] == 0) continue;
		if (check1(i)) return true;
	}
	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			if (n[i] == 0) continue;
			if (n[j] == 0) continue;
			if (check2(i, j)) return true;
		}
	}
	return false;
}

int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		memset(n, 0, sizeof(n));
		memset(e, 0, sizeof(e));
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &n[i]);
//			printf("n[%d] = %d\n", i, n[i]);
		}
		// enemy
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i == j) continue;
				e[i] += n[j];
			}
//			printf("e[%d] = %d\n", i, e[i]);
		}

		printf("Case #%d:", casenum++);
		while(rem());
		printf("\n");
		fflush(stdout);
	}
	return 0;
}

