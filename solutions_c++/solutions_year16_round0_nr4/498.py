#include <iostream>

int main() {
    long long int T, K, C, S, n_case = 1;
    std::cin >> T;
    while (T--) {
	std::cin >> K >> C >> S;
	std::cout << "Case #" << n_case++ << ":";
	if (C*S < K) {
	    std::cout << " IMPOSSIBLE\n";
	    continue;
	}
	long long  pos, i;
	for (i = 1; i <= K; i += C) {
	    pos = i;
	    for (long long j = 1; j < C; j++)
		pos = (pos-1) * K + std::min(j+i, K);
	    std::cout << ' ' << pos;
	}
	std::cout << std::endl;
    }

    return 0;
}
