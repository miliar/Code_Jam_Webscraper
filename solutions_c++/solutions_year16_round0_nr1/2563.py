#include <iostream>

#define MAX 10000

using namespace std;

bool check(bool* checked, int size, unsigned long long number) {
	char numbers[512];
	int length;
	sprintf(numbers, "%I64u", number);
	length = strlen(numbers);
	for (int i = 0; i < length; ++i) {
		checked[numbers[i] - 48] = true;
	}
	for (int i = 0; i < size; ++i) {
		if (!checked[i])
			return false;
	}
	return true;
}

void solve(int i, unsigned long long N) {
	bool checked[10] = {0};
	for (int j = 1; j < MAX; ++j) {
		unsigned long long test = N * j;
		if (check(checked, 10, test)) {
			cout << "Case #" << (i + 1) << ": " << test << endl;
			return;
		}
	}
	cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
}

int main(int argc, char* argv[]) {
	int T;
	long long N;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> N;
		solve(i, N);
	}
	return 0;
}