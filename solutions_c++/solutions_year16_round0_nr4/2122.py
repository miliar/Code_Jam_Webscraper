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

int k, c, s;

void clear() {
}

void read() {
	scanf("%d%d%d", &k, &c, &s);
}

vi solve() {
	vi res(s);
	for (int i = 1; i <= s; i++) res[i - 1] = i;
	return res;
}

int main() {
#ifdef _LOCAL_VAN
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		clear();
		read();
		vi res = solve();
		printf("Case #%d: ", i + 1);
		for (int i = 0; i < res.size(); i++) printf(i == res.size() - 1 ? "%d\n" : "%d ", res[i]);
	}
	return 0;
}