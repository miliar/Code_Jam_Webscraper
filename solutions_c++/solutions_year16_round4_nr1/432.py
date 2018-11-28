//*
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <functional>
#define MOD 1000000007
#define MAX 0x3f3f3f3f
#define MAX2 0x3f3f3f3f3f3f3f3fll
#define ERR 1e-10
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef long double ldb;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

char ord[10][10] = { "PRS", "PSR", "SPR", "SRP", "RSP", "RPS" };
int N;

int ch[1024];
vector <char> ans;
vector <char> V;

void apush(vector <char> &a, int r, int p, int s) {
	if (s == 0) {
		if (ch['R'] < ch['P']) {
			a.push_back('R');
			a.push_back('P');
		}
		else {
			a.push_back('P');
			a.push_back('R');
		}
	}
	if (p == 0) {
		if (ch['S'] < ch['R']) {
			a.push_back('S');
			a.push_back('R');
		}
		else {
			a.push_back('R');
			a.push_back('S');
		}
	}
	if (r == 0) {
		if (ch['S'] < ch['P']) {
			a.push_back('S');
			a.push_back('P');
		}
		else {
			a.push_back('P');
			a.push_back('S');
		}
	}
}
bool aa(int n, int r, int p, int s) {
	if (n == N) {
		if (r == 2 || p == 2 || s == 2) return false;

		int t = (n + 5) % 6, i;

		for (i = 0; i < 3; i++) ch[ord[t][i]] = i;

		apush(ans, r, p, s);
		return true;
	}

	int tp = (r + p - s) / 2;
	int ts = (s + p - r) / 2;
	int tr = (s + r - p) / 2;
	if (tp < 0 || ts < 0 || tr < 0) return false;
	if (!aa(n + 1, tr, tp, ts)) return false;

	int t = (n + 5) % 6, i;
	for (i = 0; i < 3; i++) ch[ord[t][i]] = i;
	for (auto it : ans) {
		if (it == 'P') apush(V, 1, 1, 0);
		if (it == 'S') apush(V, 0, 1, 1);
		if (it == 'R') apush(V, 1, 0, 1);
	}
	ans.clear();
	ans = V;
	V.clear();
	return true;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int R, P, S;
		scanf("%d %d %d %d", &N, &R, &P, &S);
		
		printf("Case #%d: ", tc);
		if (aa(1, R, P, S)) {
			for (auto it : ans) printf("%c", it);
			printf("\n");
		}
		else printf("IMPOSSIBLE\n");

		ans.clear();
	}
	return 0;
}
//*/