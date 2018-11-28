#include <iostream>
#include <string.h>
void shift(char*a, int size) {
	for (int i = size; i > 0; i--) {
		a[i] = a[i - 1];
	}
}
int main(void) {
	int T;
	std::cin >> T;

	char S[1001];
	for (int i = 0; i < T; i++) {
		std::cin >> S;

		char result[1001] = { S[0],0 };
		int len = strlen(S);
		char key = S[0];
		for (int j = 1; j < len; j++) {
			if (S[j] < key) {
				result[j] = S[j];
			}
			else {
				shift(result, j);
				key = result[0] = S[j];
			}
		}
		result[len] = 0;

		std::cout << "Case #" << i + 1 << ": " << result << std::endl;
	}

	return 0;
}