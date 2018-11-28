#include <iostream>

int main(int argc, char **argv) {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	std::cin >> T;

	for (int ca = 1; ca <= T; ca++) {
		int N;
		std::cin >> N;

		if (N == 0) {
			std::cout << "Case #" << ca << ": INSOMNIA" << std::endl;
		} else {
			int end = N;
			int found[10] = { 0 };
			int c = 0;

			while (c < 10) {
				std::string s = std::to_string(end);
				for (char ch : s) {
					if (found[ch - '0'] == 0) {
						found[ch - '0'] = 1;
						c++;
					}
				}

				end += N;
			}

			std::cout << "Case #" << ca << ": " << (end - N) << std::endl;
		}
	}
}
