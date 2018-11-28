#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <ctime>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
using namespace std;

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> pii;
typedef pair<LL, LL> pll;
#define pub push_back
#define mp make_pair
const LD EPS = 1e-9;
const int INF = INT_MAX;
const int N = 110;
const LD PI = acosl(-1.0);

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		int ans = 0;
		cin >> s;
		for (int j = 0; j < s.length() - 1; j++) {
			if (s[j] != s[j + 1]) {
				for (int k = 0; k <= j; k++) {
					if (s[k] == '+') s[k] = '-';
					else s[k] = '+';
				}
				ans++;
			}
		}
		if (s[0] == '-') ans++;
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}