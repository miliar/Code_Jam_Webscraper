#include <iostream>

using namespace std;

int newLength(char *S, int length) {
	if (0 == length) {
		return 0;
	}

	int lastIndex = 0;
	for (int i = 1; i < length; ++i) {
		if (S[lastIndex] == S[i]) {
			continue;
		}

		S[++lastIndex] = S[i];
	}

	for (int i = lastIndex; i >= 0; --i) {
		if (S[i] == '-') {
			return i + 1;
		}
	}

	return 0;
}

void dump(const char *S, int length) {
	for (int i = 0; i < length; ++i) {
		cout << S[i];
	}

	cout << endl;
}

void flip(char *S, int N) {
	char temp[100];

	/* flip */
	for (int i = 0; i < N; ++i) {
		if (S[i] == '-') {
			temp[i] = '+';
		}
		else {
			temp[i] = '-';
		}
	}

	/* swap */
	for (int i = 0; i < N; ++i) {
		S[i] = temp[N - i - 1];
	}
}

long int solve(char *S, int length) {
	int numSteps = 0;
	length = newLength(S, length);
	//dump(S, length);
	while (length > 0) {
		++numSteps;
		if (S[0] == '-') {
			flip(S, length);
		}
		else {
			flip(S, length - 1);
		}

		length = newLength(S, length);
		//dump(S, length);
	}

	return numSteps;
}

int main() {
	int T;
	char S[101];
	cin >> T;

	for (int i = 0; i < T; ++i) {
		cin >> S;
		int len = strlen(S);

		long int answer = solve(S, len);

		cout << "Case #" << i + 1 << ": ";
		cout << answer << endl;
	}

	return 0;
}