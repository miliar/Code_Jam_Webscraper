#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#define POW2(k) (1<<(k))
#define POW2L(k) (1ULL<<(k))
#define INSIDE(a, b) (POW2(a) & (b))
#define MERGE(a, b) (POW2(a) | (b))
#define LOWBIT(v) ((v)&(-(v)))
#define INF 0x3f3f3f3f
#define EPS 1e-10
using namespace std;

const double PI = acos(-1.0);

typedef pair<int, int> pii;
typedef long long LL;
typedef unsigned long long ULL;

template<class T1, class T2> inline bool ChkMax(T1 &a, const T2 &b) { if (a < b) { a = b; return true; } return false; }
template<class T1, class T2> inline bool ChkMin(T1 &a, const T2 &b) { if (a > b) { a = b; return true; } return false; }

#define MAXN 1003
#define MOD 1000000007

int var[MAXN];
bool flag[MAXN];
int svar[MAXN];
int n;

int check(int t, int res) {
	int pre = 0;
	int pos = -1;
	for (int i = 0; i < n; ++i) {
		if (var[i] == t) {
			pos = i;
			break;
		}
		if (!flag[i]) {
			++pre;
		}
	}
	flag[pos] = true;
	return min(pre, res - pre - 1);
}

int solve() {
	memcpy(svar, var, sizeof(var));
	sort(svar, svar + n);
	int key = 0;
	for (int i = 0; i < n; ++i) {
		key += check(svar[i], n-i);
	}
	return key;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
 	freopen("out", "w", stdout);
#endif

	int dataset;
	scanf("%d", &dataset);
	for (int cas = 1; cas <= dataset; ++cas) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &var[i]);
			flag[i] = false;
		}
		printf("Case #%d: %d\n", cas, solve());
	}

	return 0;
}
