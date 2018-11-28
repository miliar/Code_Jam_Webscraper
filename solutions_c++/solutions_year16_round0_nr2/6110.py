#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		string s;
		cin >> s;
		bool rev = false;
		int c = 0;
		int j = s.size() - 1;
		while (j >= 0) {
			if (s[j] == '-' && !rev) {
				c++;
				rev ^= true;
			}
			else if (s[j] == '+' && rev) {
				c++;
				rev ^= true;
			}
			j--;
		}
		cout << "Case #" << i << ": " << c << '\n';
	}
}