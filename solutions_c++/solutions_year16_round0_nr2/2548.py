#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <cassert>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

const int MAX = 200;
int n;
char s[MAX];

void clear() {
}

void read() {
	scanf("%s", s);
	n = strlen(s);
}

int solve() {
	int sw = 0;
	int res = 0;
	for (int i = n - 1; i >= 0; i--)
		if (!sw && s[i] == '-') sw ^= 1, res++;
		else if (sw && s[i] == '+') sw ^= 1, res++;
	return res;
}

int main() {
#ifdef _LOCAL_VAN
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		clear();
		read();
		int res = solve();
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}