#include <iostream>
#include <string>

int main() {
	int T;
	std::cin >> T;
	
	for (int i=1; i<=T; i++) {
		std::string S;
		std::cin >> S;
		S += "+";

		int ans = 0;
		for (size_t i=1; i<S.length(); i++)
			if (S[i - 1] != S[i])
				ans += 1;

		std::cout << "Case #" << i << ": " << ans << std::endl;
	}
}
