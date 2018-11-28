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

double ar[20];
int get_sum(int mask) {
	int sum = 0;
	while (mask) {
		if (mask & 1)
			++sum;
		mask >>= 1;
	}
	return sum;
}
double dp[20];
double ndp[20];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
//	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
//	freopen("common.in", "r", stdin);freopen("common.out", "w", stdout);
	int qq;
	cout.precision(10);
	cout << fixed;
	cin >> qq;
	for (int test = 1; test <= qq; ++test) {
		cout << "Case #" << test << ": ";
		int n, k;
		double ans = 0;
		cin >> n >> k;
		for (int i = 0; i < n; ++i)
			cin >> ar[i];
		for (int mask = 0; mask < (1 << n); ++mask) {
			if (get_sum(mask) != k)
				continue;
			for (int i = 0; i <= n; ++i)
				dp[i] = 0, ndp[i] = 0;
			dp[0] = 1;
			for (int i = 0; i < n; ++i) {
				if (!(mask & (1 << i)))
					continue;
				for (int k = n; k > 0; --k) {
					ndp[k] = dp[k - 1] * ar[i] + dp[k] * (1.0 - ar[i]);
				}
				ndp[0] = dp[0] * (1.0 - ar[i]);
				for (int k = 0; k <= n; ++k)
					dp[k] = ndp[k];
			}
			ans = max(ans, dp[k / 2]);
		}
		cout <<ans <<'\n';
	}


	return 0;
}