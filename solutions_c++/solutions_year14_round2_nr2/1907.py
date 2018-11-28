#pragma comment(linker, "/STACK:836777216")

#define INF (long long)1e18
#define EPS 1e-15
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <memory.h>

using namespace std;

int tests;
int a, b, k;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cin >> a >> b >> k;
		int ans = 0;
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if ((i & j) < k) {
					ans++;
				}
			}
		}
		cout << "Case #" << test << ": " << ans << '\n';
	}
	return 0;
}