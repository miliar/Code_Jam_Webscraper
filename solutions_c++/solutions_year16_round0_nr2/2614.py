#include <iostream>

using namespace std;

void flip(char* pancakes, int pos) {
	for (int i = 0; i <= pos; ++i) {
		pancakes[i] = (pancakes[i] == '-' ? '+' : '-');
	}
}

int check(char* pancakes, int size) {
	for (int i = size - 1; i >= 0; --i) {
		if (pancakes[i] == '-') {
			return i;
		}
	}
	return -1;
}

void solve(int C, char* pancakes, int size) {
	int flips = 0, pos;
	while ((pos = check(pancakes, size)) >= 0) {
		flip(pancakes, pos);
		++flips;
	}
	cout << "Case #" << C << ": " << flips << endl;
}

int main(int argc, char* argv[]) {
	int T;
	char pancakes[128];
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> pancakes;
		solve(i + 1, pancakes, strlen(pancakes));
	}
	return 0;
}