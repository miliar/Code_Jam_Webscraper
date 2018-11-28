#include <iostream>
#include <algorithm>

bool test(const std::string & S) {
	return std::find(S.begin(), S.end(), '-') == S.end();
}

void flip(std::string & S, size_t s, int K) {
	if (s + K > S.size()) return;
	for (size_t i = s ; i < s + K ; ++i)
		S[i] = (S[i] == '-')?'+':'-';
}

int solve(std::string S, int K) {
	int ret = 0;
	for (size_t i = 0 ; i < S.size(); ++i) {
		if (S[i] == '-') {
			flip(S, i, K);
			ret++;
		}
	}
	if (test(S)) return ret;
	return -1;
}

int main(int argc, const char *argv[])
{
	int T;
	int K;
	std::string S;
	std::cin >> T;
	for (int tcase = 1 ; tcase <= T ; ++tcase) {
		std::cout << "Case #" << tcase << ": ";
		std::cin >> S >> K;
		int sol = solve(S, K);
		if (sol < 0) std::cout << "IMPOSSIBLE" << std::endl;
		else std::cout << sol << std::endl;
	}
	return 0;
}
