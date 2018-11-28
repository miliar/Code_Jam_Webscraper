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
	freopen("output.txt", "w", stdout);
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

int n, m;
set<lint> used;

void read() {
	cin >> n >> m;
}

lint is_prime(lint v) {
	if (v == 1)
		return false;
	if (v == 2)
		return true;
	lint q = sqrt(v) + 1;
	forab(i, 2, q) {
		if (v % i == 0)
			return i;
	}
	return 0;
}

string i2s(lint v) {
	int p = 1;
	string s;
	while (v >= p) {
		s += (v & p) ? '1' : '0';
		p <<= 1;
	}
	reverse(all(s));
	return s;
}

lint to_dec(lint v, int base) {
	lint p = 1;
	lint pbase = 1;

	lint res = 0;
	while (p <= v) {
		if (v & p)
			res += pbase;
		p <<= 1;
		pbase *= base;
	}
	return res;
}

bool check(lint v, vector<int> &vec) {
	forab(i, 2, 10) {
		lint vdec = to_dec(v, i);
		lint val = is_prime(vdec);
		if (val == 0)
			return false;
		vec.push_back(val);
	}
	return true;
}

bool solve(int v, vector<int> &ans) {
	if (used.count(v))
		return false;

	ans.clear();
	if (check(v, ans)) {
		used.insert(v);
		string s = i2s(v);

		printf("%s ", &s[0]);
		forn(i, sz(ans)) {
			printf("%ld ", ans[i]);
		}
		printf("\n");

		return true;
	}
	return false;
}

void solve() {
	vector<int> ans;
	while (1) {
		int len = n - 2;
		lint v = (rand() * rand()) % (1 << len);
		v = (1 << (len + 1)) + (v << 1) + 1;
		
		if (solve(v, ans)) {
			if (used.size() == m)
				return;
		}
	}

	/*forn(i, 1 << (n - 2)) {
		lint v = (1 << (n - 1)) + (i << 1) + 1;

		if (solve(v, ans)) {
			if (used.size() == m)
				return;
		}
	}*/
}

int main() {
	freopen("");

	int t;
	cin >> t;
	forn(i, t) {
		printf("Case #%d:\n", i + 1);
		read();
		solve();
	}

	return 0;
}