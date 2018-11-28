#pragma comment(linker, "/STACK:500000000")
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <assert.h>
#include <bitset>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <unordered_set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

#define y0 y0ChloeGraceMoretz
#define y1 y1ChloeGraceMoretz
#define ll long long
int nextInt() { int n; scanf("%d", &n); return n; }
ll nextLong() { ll n; scanf("%lld", &n); return n; }
const double PI = acos(-1.0);
const double EPS = 1e-9;
const int INF = (int)2e9;

double p[20];
char mask[20];
bool isFound;
int n;

bool check() {
	string cur = "";
	for (int i = 0; i < (1 << n); ++i) {
		cur += mask[i];
	}
	while (cur.length() > 1) {
		string tmp = "";
		for (int i = 0; i < cur.length(); i += 2) {
			if (cur[i] == cur[i + 1]) {
				return false;
			}
			if ((cur[i] == 'R' && cur[i + 1] == 'S')
				|| (cur[i] == 'S' && cur[i + 1] == 'R')) {
				tmp += 'R';
			} else if ((cur[i] == 'S' && cur[i + 1] == 'P')
				|| (cur[i] == 'P' && cur[i + 1] == 'S')) {
				tmp += 'S';
			} else {
				tmp += 'P';
			}
		}
		cur = tmp;
	}
	return true;
}

void f(int pos, int r, int p, int s) {
	if (isFound) {
		return;
	}
	if (r + p + s == 0) {
		if (check()) {
			isFound = true;
			for (int i = 0; i < (1 << n); ++i) {
				printf("%c", mask[i]);
			}
			printf("\n");
		}
		return;
	}
	if (p > 0) {
		mask[pos] = 'P';
		f(pos + 1, r, p - 1, s);
	}
	if (r > 0) {
		mask[pos] = 'R';
		f(pos + 1, r - 1, p, s);
	}
	if (s > 0) {
		mask[pos] = 'S';
		f(pos + 1, r, p, s - 1);
	}
}

int main() {
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int r, p, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);
		printf("Case #%d: ", tt);
		isFound = false;
		f(0, r, p, s);
		if (!isFound) {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}