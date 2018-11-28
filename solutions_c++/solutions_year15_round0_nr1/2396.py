#include <iostream>
#include <string>
#include <cstdio>

using namespace std;


int main() {
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;

	for (int test = 0; test < t; test++) {
		cout << "Case #" << test + 1 << ": ";

		int n;
		string s;
		cin >> n;
		cin >> s;

		int sum = 0, ans = 0;
		for (int i = 0; i < n + 1; i++) {
			if (i > sum)
				ans++, sum++;
			sum += s[i] - '0';
		}
		cout << ans << endl;
	}
}