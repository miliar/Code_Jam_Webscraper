#include <iostream>
#include <string>
#include <map> 
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <deque>
#include <memory.h>


using namespace std;

#define ll long long
#pragma comment(linker, "/STACK:64000000")

const int maxn = 1 << 17;
const int inf = 1000000007;
const int mod = 1000000007;

int n;
ll p;

ll geta(int n, ll p) {
	if ((1LL << n) == p) return p - 1;
	ll csum = 0, ans = 1;
	int ci = n - 1;
	while (ci >= 0) {
		csum += (1LL << ci);
		ci--;
		if (p > csum)
			ans = 2 * ans + 1;
	}
	return ans - 1;
}

ll getb(int n, ll p) {
	if (p == (1LL << n)) return (1LL << n) - 1;
	ll place = (1LL << n) / 2;
	ll ans = 1;
	while (place > p) {
		place >>= 1;
		ans = ans * 2 + 1;
	}
	return (1LL << n) - ans - 1;
}

pair<ll, ll> solve() {
	ll a = -1, b = -1;
	a = geta(n, p);
	b = getb(n, p);
	return make_pair(a, b);
}

int fct(int x) {
	return x ? fct(x - 1) * x : 1;
}

vector<int> mn, mx;

void rec(vector<int> a, int add = 0) {
	if (a.size() == 1) {
		mn[a[0]] = min(mn[a[0]], add);
		mx[a[0]] = max(mx[a[0]], add);
		return;
	}
	vector<int> b, c;
	for (int i = 0; i < a.size(); i += 2) {
		b.push_back(min(a[i], a[i + 1]));
		c.push_back(max(a[i], a[i + 1]));
	}
	rec(b, add);
	rec(c, add + b.size());
}

pair<int, int> slowsolve() {
	mn.assign(1 << n, 1 << n);
	mx.assign(1 << n, 0);
	vector<int> a(1 << n);
	for (int i = 0; i < 1 << n; i++) a[i] = i;
	for (int it = 0; it < fct(1 << n); it++) {
		rec(a);
		next_permutation(a.begin(), a.end());
	}
	pair<int, int> o;
	o.first = 0; o.second = 0;
	for (int i = 0; i < 1 << n; i++) {
		if (mx[i] + 1 <= p) o.first = i;
		if (mn[i] + 1 <= p) o.second = i;
	}
	return o;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
    int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cin >> n >> p;
		pair<ll, ll> o = solve();
		cout << o.first << " " << o.second << endl;
	}
	return 0;
}