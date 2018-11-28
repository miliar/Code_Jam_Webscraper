#include <iostream>
#include <set>

int main() {
	int T;
	std::cin >> T;
	
	for (int i=1; i<=T; i++) {
		int N;
		std::cin >> N;

		if (N == 0) {
			std::cout << "Case #" << i << ": INSOMNIA" << std::endl;
		} else {
			std::set<int> set;
			int X = N;

			while (set.size() < 10) {
				int C = X;
				while (C > 0) {
					set.insert(C % 10);
					C /= 10;
				}
				X += N;
			}

			std::cout << "Case #" << i << ": " << X - N << std::endl;
		}
	}
}
