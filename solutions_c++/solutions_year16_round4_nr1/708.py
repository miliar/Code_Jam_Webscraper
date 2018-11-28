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

string dp[3][1 << 5][1 << 5][1 << 5];
int used[3][1 << 5][1 << 5][1 << 5];
inline string din(int last, int q, int w, int e) {
	if (used[last][q][w][e])
		return dp[last][q][w][e];
	used[last][q][w][e] = 1;
	string &da = dp[last][q][w][e];
	int sum = q + w + e;
	if (sum == 1) {
		if (last == 0) {
			if (q) {
				da = "P";
			}
			return da;
		}
		if (last == 1) {
			if (w)
				da = "R";
			return da;
		}
		if (e)
			da = "S";
		return da;
	}
	int dsum = sum / 2;
	int to = last + 1;
	to %= 3;
	for (int i = 0; i <= q; ++i) {
		for (int j = 0; j <= w && j + i <= dsum; ++j) {
			int k = dsum - i - j;
			if (k > e)
				continue;
			string z, x;
			
				z = din(last, i, j, k);
				x = din(to, q - i, w - j, e - k);
				if (z.size() != 0 && x.size() != 0) {
					if (da.empty())
						da = min(z + x, x + z);
					else
						da = min(da, min(z + x, x + z));
				}
			
		}
	}
	return da;
}
inline int check(int a) {
	if (!a)
		return 0;
	while (a != 1) {
		if ((a & 1))
			return 0;
		a >>= 1;
	}
	return 1;
}

string ans[3][13];
int sum[3][13][3];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
//	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
//	freopen("common.in", "r", stdin);freopen("common.out", "w", stdout);
	/*for (int i = 0; i < 30; ++i) {
		for (int j = 0; j < 30; ++j) {
			for (int k = 0; k < 30; ++k) {
				if (!check(i + j + k))
					continue;
				for (int q = 0;  q < 3; ++q) {
					string w = din(q, i, j, k);
					if (w.empty())
						continue;
					cout << q << ' ' << i << ' ' << j << ' ' << k << ' ' << w << '\n';
					
				}
			}
		}
	}*/
	ans[0][0] = "P";
	ans[1][0] = "R";
	ans[2][0] = "S";
	sum[0][0][0] = 1;
	sum[1][0][1] = 1;
	sum[2][0][2] = 1;
	for (int i = 1; i <= 12; ++i) {
		for (int j = 0; j < 3; ++j) {
			int to = (j + 1) % 3;
			for (int k = 0; k < 3; ++k) {
				sum[j][i][k] = sum[j][i - 1][k] + sum[to][i- 1][k];
			}
			string &a = ans[j][i - 1];
			string &b = ans[to][i - 1];
			if (a < b) {
				ans[j][i] = a + b;
			}
			else
				ans[j][i] = b + a;
		//	cout << i << ' ' << j << ' ' << ans[j][i] << '\n';
		}
	}
	int qq;
	cin >> qq;
	for (int test = 1; test <= qq; ++test) {
		int n;
		int j, i, k;
		cin >> n >> j >> i >> k;
		cout << "Case #" << test << ": ";
		int flag = 1;
		for (int z = 0; z < 3; ++z) {
			if (sum[z][n][0] == i && sum[z][n][1] == j && sum[z][n][2] == k) {
				cout << ans[z][n] << '\n';
				flag = 0;
				break;
			}
		}
		if (flag)
			cout << "IMPOSSIBLE\n";
	}


	return 0;
}