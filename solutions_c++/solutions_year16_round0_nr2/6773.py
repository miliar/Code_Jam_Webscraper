#include <iostream>
#include <cstdlib>
#include <string>

int solveProblem(const std::string& S) {
	char wrong = '-';
	int flips = 0;

	for (int i = S.size()-1; i >= 0; --i) {
		if (S[i] == wrong) {
			++flips;
			wrong = wrong == '-' ? '+' : '-';
		}
	}

	return flips;
}

int main () {
    int T;
    std::cin >> T;

    for (int test = 1; test <= T; ++test) {
        std::string S;
        std::cin >> S;


        std::cout << "Case #" << test << ": " << solveProblem(S) << std::endl;

    }

    return EXIT_SUCCESS;
}
