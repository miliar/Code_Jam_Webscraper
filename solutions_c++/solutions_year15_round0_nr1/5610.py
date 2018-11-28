#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldb;

int cnt[1001], T, smax;
string s;
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> smax >> s;
		for (int i = 0; i < smax + 1; i++)
			cnt[i] = s[i] - '0';
		int ans = 0, total = cnt[0];
		for (int i = 1; i < smax + 1; i++) {
			if (total < i)	{
				ans += i - total;
				total += i - total;
			}
			total += cnt[i];
		}
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}