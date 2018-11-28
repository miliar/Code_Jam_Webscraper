#include <algorithm>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define SIZE(v) ((int)(v).size())

#define BEGIN(v) ((v).begin())
#define END(v) ((v).end())
#define ALL(v) BEGIN(v),END(v)
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) SORT(v);(v).erase(unique(ALL(v)),END(v))

#define FOR(i,l,r) for(int i=(l);i<(r);i++)
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)

const int MAXN = 23;
const int MAXMASK = 1 << MAXN;

int n;
long double price[MAXMASK];

int getDist(int x, int y) {
	return x <= y ? y - x : y - x + n;
}

long double getPrice(int mask) {
	if (price[mask] > -.5) return price[mask];
	price[mask] = 0;
	int nxt = -1;
	FOR(i, 0, n) if (!(mask & (1 << i))) {
		nxt = i; break;
	}
	for (int i = n - 1; i >= 0; i--) {
		if (!(mask & (1 << i))) nxt = i;
		price[mask] += n - getDist(i, nxt) + getPrice(mask | (1 << nxt));
	}
	price[mask] /= n;
	return price[mask];
}

int main() {
	int taskNumber; scanf("%d", &taskNumber);
	for (int taskIdx = 1; taskIdx <= taskNumber; taskIdx++) {
		char op[MAXN]; scanf("%s", op);
		n = strlen(op);
		int mask = 0;
		FOR(i, 0, n) if (op[i] == 'X') mask |= 1 << i;
		FOR(mask, 0, 1 << n) price[mask] = -1;
		price[(1 << n) - 1] = 0;
		printf("Case #%d: %.16Lf\n", taskIdx, getPrice(mask));
	}
	return 0;
}
