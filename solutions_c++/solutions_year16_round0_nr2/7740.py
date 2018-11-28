/*
 * Revenge of the Pancakes.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: Mostafa
 */
#include<bits/stdc++.h>

using namespace std;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long long ll;

int di[] = { 0, 0, 0, -1, 1 }, dj[] = { 0, 1, -1, 0, 0 };

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
	return a * (b / gcd(a, b));
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);

	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		string s;
		cin >> s;
		int res = 0, cntm = 0;
		int sz = s.size(), r = sz - 1, l = 0;
		for (int i = 0; i < sz; ++i) {
			if (s[i] == '-')
				cntm++;
		}
		while (s[r] == '+' && r >= 0)
			r--;
		if (r == -1) {
			cout << "Case #" << cs << ": " << 0 << endl;
			continue;
		}
		while (s[l] == '-' && l < sz) {
			l++;
		}
		if (l - r == 1) {
			cout << "Case #" << cs << ": " << 1 << endl;
			continue;
		}
		for (int i = sz - 1; i >= 0; i--) {
			if (s[i] == '-') {
				r = i;
				break;
			}
		}
		while (cntm > 0) {
			for (int u = sz - 1; u >= 0; u--) {
				if (s[u] == '-') {
					r = u;
					break;
				}
				r = -1;
			}
			if (s[0] == '+') {
				int i = 0;
				while (s[i] == '+') {
					s[i++] = '-';
					cntm++;
				}
				res++;
			} else {
				res++;
				string s2 = s;
				int i = 0, j = r;
				for (int k = j; k >= 0; k--) {
					if (s[i] == '-') {
						s2[j] = '+';
						cntm--;
					} else {
						s2[j] = '-';
						cntm++;
					}
					j--;
					i++;
				}

				s = s2;
			}
		}
		cout << "Case #" << cs << ": " << res << endl;

	}

	return 0;
}
