#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <memory.h>
#include <set>
#include <ctime>
#include <map>
#include <cstring>
#include <iterator>
#include <queue>
#include <assert.h>
#include <unordered_map>
#include <unordered_set>
#include <bitset>

using namespace std;



#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define ull unsigned long long
#pragma comment(linker, "/STACK:64000000")

typedef long double ld;
typedef pair<ld, ld> pldld;
typedef long long ll;
typedef pair<ll, ll> pll;


typedef unsigned int ui;
typedef unsigned char uc;
const int infi = 1e9 + 7;
const ll infl = 1e18;
const double eps = 1e-7;

int ar[10];
int perm[10];
int mask[10];
int check(int mask1, int mask2) {
	int ans = 0;
	for (int i = 0; i < 4; ++i, mask1 >>= 1, mask2 >>= 1) {
		if (mask1 &  1) {
			if (mask2 & 1)
				continue;
			++ans;
		}
		else {
			if (mask2 & 1)
				return -1;
		}
	}
	return ans;
}
int check_used(int q, int n, int fr) {
	if (q == n)
		return (fr == 0);
	int flag = 1;
	int cur = perm[q];
	int ms = fr & mask[cur];
	if (ms == 0)
		return 0;
	for (int i = 0; i < n; ++i) {
		if (!(ms & (1 << i)))
			continue;
		if (!check_used(q + 1, n, fr ^ (1 <<i)))
			return 0;
	}
	return 1;
}
int g_ans;
inline void rec(int q, int n, int ans) {
	if (q == n) {
		for (int i = 0; i < n; ++i)
			perm[i] = i;
		if (!check_used(0, n, (1 << n) - 1))
			return;
		while (next_permutation(perm, perm + n)) {
			if (!check_used(0, n, (1 << n) - 1)) {
				return;
			}
		}
		g_ans = min(g_ans, ans);
		return;
	}
	for (int cur_mask = 0; cur_mask < (1 << n); ++cur_mask) {
		int cost = check(cur_mask, ar[q]);
		if (cost == -1)
			continue;
		mask[q] = cur_mask;
		rec(q + 1, n, ans + cost);
	}
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
//	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
//	freopen("common.in", "r", stdin);freopen("common.out", "w", stdout);
	int qq;
	cout.precision(10);
	perm[0] = 0, perm[1] = 1;
	int a = next_permutation(perm, perm + 2);
	int b = next_permutation(perm, perm + 2);
	cout << fixed;
	cin >> qq;
	for (int test = 1; test <= qq; ++test) {
		cout << "Case #" << test << ": ";
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i) {
			ar[i] = 0;
			for (int j = 0; j < n; ++j) {
				char c;
				cin >> c;
				if (c == '1')
					ar[i] |= (1 << j);
			}
		}
		g_ans = infi;
		rec(0, n, 0);
		cout << g_ans << '\n';
	}


	return 0;
}