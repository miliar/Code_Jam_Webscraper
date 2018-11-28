#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <sstream>

#include <vector>
#include <algorithm>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <string>
#include <cstring>
#include <string.h>

#include <time.h>
#include <cassert>
#include <memory.h>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define fornd(i, n) for(int i = (int)(n-1); i >= 0; i--)
#define forab(i, a, b) for(int i = (int)a; i <= (int)b; i++)
#define forabd(i, b, a) for(int i = (int)b; i >= (int)a; i--)

#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a).size())
#define _(a, val) memset(a, val, sizeof(a))
#define all(a) (a).begin(), (a).end()

typedef long long lint;
typedef long double ld;

void freopen(string s) {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#else
	if (s != "")
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

const int NMAX = 100100;
const int INF = 1000 * 1000 * 1000;
const lint LINF = (lint)INF*(lint)INF;

int cnt_d = 0;
bool used[10];

int count(lint v) {
	while (v != 0) {
		int d = v % 10;
		v /= 10;
		if (!used[d])
			++cnt_d;
		used[d] = true;
	}
	return cnt_d;
}

lint solve(int n) {
	cnt_d = 0;
	_(used, 0);

	lint i = 1;
	for (; count(i * n) < 10; ++i);

	return i * n;
}

void read() {
	int t, n;
	cin >> t;
	forab(i, 1, t) {
		scanf("%d", &n);
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", i);
		else {
			lint ans = solve(n);
			printf("Case #%d: %ld\n", i, ans);
		}
	}
}

void brute() {
	forab(i, 1, 1000000) {
		solve(i);
	}
}

int main() {
	freopen("A-large");

	//brute();
	read();
	//solve();

	return 0;
}