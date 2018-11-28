#include <iostream>
#include <string>

int main() {
	int t, c = 0;
    std::cin >> t;
	std::string s;
    while (t--) {
		int k, r = 0;
		std::cin >> s >> k;
		int len = s.size(), e = len - k + 1;
		for (int i = 0; i < e; i++) {
			if (s[i] == '-') {
				r++;
				for (int j = i, f = i + k; j < f; j++) {
					s[j] ^= '-' ^ '+';
				}
			}
		}
		bool ok = true;
		for (int i = e; i < len; i++) {
			if (s[i] == '-') {
				ok = false;
				break;
			}
		}
		c++;
		std::cout << "Case #" << c << ": ";
		if (ok)
			std::cout << r << std::endl;
		else
			std::cout << "IMPOSSIBLE" << std::endl;
    }
    return 0;
}
