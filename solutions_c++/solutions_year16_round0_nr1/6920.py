#include <stdio.h>
#include <iostream>

using namespace std;

int digits(long long v, int *done, int doneCount) {

	while (v > 0) {
		long long digit = v % 10;
		if (done[digit] == 0) {
			done[digit]++;
			doneCount++;
		}
		v /= 10;
	}
	return doneCount;
}

int run(long long N) {
	if (N == 0) return 0;
	int done[10];
	int doneCount = 0;
	for (int i = 0; i < 10; i++) done[i] = 0;
	long long NN = N;
	long long iter = 1;
	while (true) {
		doneCount = digits(NN, done, doneCount);
		if (doneCount == 10) return NN;
		iter++; NN += N;
	}
}

int main(int argc, char **argv) {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		cout << "Case #" << t << ": ";
		int result = run(N);
		if (result == 0) {
			cout << "INSOMNIA" << endl;
		} else {
			cout << result << endl;
		}
	}
	return 0;
}
