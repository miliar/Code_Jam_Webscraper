#include <iostream>
#include <algorithm>

int main(void)
{
	int T;
	char S[200];

	std::cin >> T;

	for (int i = 0; i < T; i++) {
		std::cin >> S;

		int len = strlen(S);
		int cnt = 0;
		for (int j = 0; j < len - 1; j++) {
			if (S[j] != S[j + 1]) {
				cnt++;
			}
		}
		if (S[len - 1] == '-') {
			cnt++;
		}

		std::cout << "Case #" << i+1 << ": " << cnt << std::endl;

	}

	return 0;
}

