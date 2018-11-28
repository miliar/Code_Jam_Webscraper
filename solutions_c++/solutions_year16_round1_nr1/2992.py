#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int g = 1; g <= t; ++g) {
		string word;
		cin >> word;
		string ans = "";
		ans += word[0];
		for (int i = 1; i < word.length(); ++i) {
			if (word[i] >= ans[0])
				ans = word[i] + ans;
			else
				ans += word[i];
		}
		cout << "Case #" << g << ": " << ans << '\n';
	}

	return 0;
}