#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <cstdio>
#include <limits>
#define _USE_MATH_DEFINES
#define vi vector<int>
using namespace std;
int main () {
	freopen ("D:\\Internet\\B-large.in", "r", stdin);
	freopen ("B-output-large.txt", "w", stdout);
	string s;
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> s;
		int n = s.length();
		bool tStat = s[0] == '+';
		int ans = 0;
		for (int i = 0; i < n - 1; i++) {
			if (s[i] != s[i + 1])
				ans++;
			tStat = s[i + 1] == '+';
		}
		if (!tStat)
			ans++;
		cout << "Case #" << t << ": " << ans << endl;
	}
}