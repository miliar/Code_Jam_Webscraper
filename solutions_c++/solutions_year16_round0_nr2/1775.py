#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main(void) {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";
		std::string S;
		std::cin >> S;
		int n = 0;
		int form;
		char a = S[0], b = S[S.length()-1];
		if (a == '+' && b == '-') form = 1; // (+-)^n
		else if (a == '-' && b == '+') form = 2; // (-+)^n
		else if (a == '+') form = 3; // (+-)^n+
		else form = 4; // (-+)^n-

		char prev = S[S.length()-1];
		bool ends = true;
		for (int i = S.length() - 2; i >= 0; i--) {
			if (prev != S[i]) {
				if (ends) n++;
				ends = !ends;
				prev = S[i];
			}
		}
		n <<= 1;
		n += (form == 2 ? -1 : form == 4 ? 1 : 0);
		std::cout << n;
		std::cout << std::endl;
	}
	return 0;
}
