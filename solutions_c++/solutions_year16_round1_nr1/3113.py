#include<iostream>
#include<string>

void solve(int c) {
	std::string s, ans = "";
	std::cin >> s;

	for (int i = 0; i < s.length(); i++) {
		std::string tmp = ans, tmp2 = "";
		tmp += s[i];
		tmp2 += s[i] + ans;

		if (tmp > tmp2) {
			ans = tmp;
		} else {
			ans = tmp2;
		}
	}
	std::cout << "Case #" << c + 1 << ": " << ans << std::endl;
}

int main() {
	int n;
	std::cin >> n;

	for (int i = 0; i < n; i++) {
		solve(i);
	}
}