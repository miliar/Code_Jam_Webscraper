#include <cstdio>

#include <iostream>
#include <algorithm>
#include <string>

int solve(const std::string& pc)
{
	if (std::find(pc.begin(), pc.end(), '-') == pc.end()) {
		return 0;
	}

	int sol = 0;
	char last = *pc.begin();
	for (char c : pc) {
		if (c != last) {
			++sol;
		}
		last = c;
	}

	sol += last == '-' ? 1 : 0;

	return sol;
}

int main()
{
	int c;
	std::cin >> c;
	std::string str;
	std::getline(std::cin, str);
	for (int i = 1; i <= c; i++) {
		std::getline(std::cin, str);
		printf("Case #%d: %d\n", i, solve(str));
	}
}
