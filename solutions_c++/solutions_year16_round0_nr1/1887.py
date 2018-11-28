#include <iostream>
using namespace std;
int main() {
	int T, N;
	cin >> T;
	for (int ccc = 1; ccc <= T; ccc++) {
		cin >> N;
		cout << "Case #" << ccc << ": ";
		if (N == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		int ayy = 0b1111111111;
		int rofl[] = { 0b1111111110,
		               0b1111111101,
		               0b1111111011,
		               0b1111110111,
		               0b1111101111,
		               0b1111011111,
		               0b1110111111,
		               0b1101111111,
		               0b1011111111,
		               0b0111111111 };
		int p = 1;
		while (ayy != 0) {
			int x = N * p;
			while (x != 0) {
				ayy = ayy & rofl[x % 10];
				x /= 10;
			}
			if (ayy == 0) break;
			p++;
		}
		cout << N*p << endl;
	}
	return 0;
}
