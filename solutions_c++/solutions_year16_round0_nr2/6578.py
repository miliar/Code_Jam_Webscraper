#include <iostream>

int main(int argc, char **argv) {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	std::cin >> T;

	for (int ca = 1; ca <= T; ca++) {
		std::string stack;
		std::cin >> stack;

		int count = 0;
		for (int i = 1; i < stack.size(); i++) {
			if (stack[i] != stack[i - 1]) {
				count++;
			}
		}
		if (stack[stack.size() - 1] == '-') {
			count++;
		}

		std::cout << "Case #" << ca << ": " << count << std::endl;
	}
}
