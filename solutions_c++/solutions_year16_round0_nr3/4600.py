#include <iostream>
#include <string>


using namespace std;

typedef unsigned uint32;

void printBaseStr(int N) {
	cout << "1";
	for (int i = 0; i < N - 2; i++)
		cout << "0";
	cout << "1";
}

void printStr(int N, int k, int i, int j) {
	char s[32];
	s[0] = '1';
	s[N - 1] = '1';
	for (int z = 0; z < k; z++)
		s[2 * z + 1] = s[2 * z + 2] = '1';
	for (int z = 2 * k + 1; z < N - 1; z++)
		s[z] = '0';
	// place '1's
	s[2 * k + 2 * i + 1] = '1';
	s[2 * k + 2 * j + 2] = '1';

	//cout << "(" << i << ", " << j << ", " << k << ")  ";

	for (int z = 0; z < N; z++)
		cout << s[z];
}

void printDiv() {
	for (int i = 2; i <= 10; i++)
		cout << " " << i + 1;
	cout << endl;
}


void solve() {
	int N, J; cin >> N >> J;
	int count = 1;
	printBaseStr(N); printDiv();
	int k = 0, i = 0, j = 0, b = N / 2 - 1;
	while (count < J) {
		printStr(N, k, i, j);
		printDiv();
		count++;

		if (i < b - 1)
			i++;
		else if (j < b - 1) {
			i = 0; j++;
		}
		else {
			i = j = 0; k++; b--;
		}
	}
}

int main(int argc, char** argv) {
	int T;
	cin >> T; // number of test cases
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": " << endl;
		solve();
	}

}

	