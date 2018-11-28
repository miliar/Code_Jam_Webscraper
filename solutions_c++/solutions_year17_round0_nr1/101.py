#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:10034217728")
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

void flip(string& s, int pos) {
	if (s[pos] == '-') {
		s[pos] = '+';
	}
	else {
		s[pos] = '-';
	}
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int n;
	cin >> n;
	string s;
	for (int q = 0; q < n; q++) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		for (int i = 0; i < s.size(); i++) {
			if (i + k - 1 >= s.size()) break;
			if (s[i] == '-') {
				for (int j = i; j < i + k; j++) {
					flip(s, j);
				}
				ans++;
			}
		}
		printf("Case #%d: ", q + 1);
		if (s.find('-') == string::npos) {
			printf("%d\n", ans);
		}
		else {
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}