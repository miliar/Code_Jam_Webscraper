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

int solve(string &s) {
	int ans = 0;
	if (s[0] == '-')
		ans = -1;

	int cnt = s[0] == '-' ? 1 : 0;
	forab(i, 1, sz(s) - 1) {
		if (s[i] != s[i - 1] && s[i] == '-') {
			cnt++;
		}
	}

	ans += 2 * cnt;
	return ans;
}

char chs[101];

void read(int t) {
	scanf("%s", chs);

	string s(chs);

	int ans = solve(s);

	printf("Case #%d: %d\n", t, ans);
}

string i2s(int v, int len) {
	int p = 1;
	string res = "";
	forn(i, len) {
		res += (v & p) ? '-' : '+';
		p <<= 1;
	}
	return res;
}

int gen(int len) {
	int val = rand() & ((1 << len) - 1);
	return val;
}

int gen() {
	int len = rand() % 15;
	return gen(len);
}

int _u[1000000];

void bfs(int v, int len, int cnt) {
	queue< pair<int, int> > q;
	q.push(mp(v, cnt));
	_(_u, 255);
	_u[v] = cnt;

	int p = (1 << len) - 1;
	while (!q.empty()) {
		int v = q.front().first;
		int cnt = q.front().second;
		q.pop();

		forab(i, 1, len) {
			int p1 = (1 << i) - 1;
			int p2 = p << i;

			int v1 = (~v) & p1;
			int v2 = v & p2;

			int _v = v1 | v2;
			if (_u[_v] != -1)
				continue;
			_u[_v] = cnt + 1;
			q.push(mp(_v, cnt + 1));
		}
	}
}

int solve1(int v) {
	return _u[v];
}

void brute() {
	srand(228);
	
	int step = 0;
	while (1) {
		step++;
		int len = rand() % 15 + 1;

		bfs(0, len, 0);

		forn(v1, 1 << len) {
			string v2 = i2s(v1, len);
			int ans1 = solve1(v1);
			int ans2 = solve(v2);

			if (ans1 != ans2) {
				cout << step << endl << endl;

				cout << v1 << endl;
				cout << ans1 << endl;
				cout << endl;
				cout << v2 << endl;
				cout << ans2 << endl;
				return;
			}
		}
	}
}

int main() {
	freopen("B-large");

	//brute();

	int t;
	scanf("%d", &t);
	forn(i, t) {
		read(i + 1);
	}

	return 0;
}