#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main(void) {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";
		int N;
		std::cin >> N;
		int N2 = (2*N-1)*N;
		std::vector<int> hs(N2);
		for (int i = 0; i < N2; i++) {
			std::cin >> hs[i];
		}
		std::sort(hs.begin(), hs.end(), [](int a, int b) { return a < b;});
		int numb = 1;
		std::vector<int> res;
		for (int i = 1; i < N2; i++) {
			if (hs[i] == hs[i-1]) numb++;
			else {
				if (numb % 2 == 1) res.push_back(hs[i-1]);
				numb = 1;
			}
		}
		if (numb % 2 == 1) res.push_back(hs[N2-1]);
		std::sort(res.begin(), res.end(), [](int a, int b) {return a < b;});
		for (int i = 0; i < N; i++)
			std::cout << res[i] << " ";
		std::cout << std::endl;
	}
	return 0;
}
