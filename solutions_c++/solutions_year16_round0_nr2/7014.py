#include <stdio.h>
#include <iostream>

using namespace std;

int run(const char *signs) {
	int L = strlen(signs);
	int flipCount = 0;
	for (int i = 1; i < L; i++) {
		if (signs[i] != signs[i - 1]) flipCount++;
	}
	if (signs[L - 1] == '-') flipCount++;
	return flipCount;
}

int main(int argc, char **argv) {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		char N[256];
		cin >> N;
		cout << "Case #" << t << ": ";
		int result = run(N);
		cout << result << endl;
	}
	return 0;
}
