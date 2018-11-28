#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin >> t;
	for (int k = 0; k < t; ++k) {
		int ans = 0;
		int cur = 0;
		int n;
		cin >> n;
		string s;
		cin >> s;
		for (int i = 0; i <= n; ++i) {
			if (cur < i) {
				ans += (i - cur);
				cur = i;
			}
			cur += (s[i] - '0');
		}
		cout << "Case #" << k + 1 << ": " << ans << endl;
	}
}