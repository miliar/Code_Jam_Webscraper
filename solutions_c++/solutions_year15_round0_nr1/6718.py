#include <iostream>
#include <cstdio>
#include <vector>

int main() {
	std::freopen("in", "r", stdin);
	std::freopen("out", "w", stdout);
	std::ios_base::sync_with_stdio(false);
	int cases;
	std::cin >> cases;
	for (int c = 1; c <= cases; c++) {
		std::vector<int> people;
		int count;
		std::cin >> count;
		for (int i = 0; i < count + 1; i++) {
			char next;
			std::cin >> next;
			people.push_back(next - '0');
		}

		int p = 0;
		int add = 0;
		for (int i = 0; i < people.size(); i++) {
			if (people[i] == 0)
				continue;

			if (p < i) {
				add += i - p;
				p += i - p;
			}

			p += people[i];
		}

		std::printf("Case #%d: %d\n", c, add);
	}

	return 0;
}
