#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int T;
	cin >> T;
	int temp1 = T;
	while (T--) {
		int a, N;
		cin >> a >> N;
		int b[N];
		for (int i = 0; i < N; i++)
			cin >> b[i];
		sort(b, b + N);
		int count = 0, cheat = 0;
		if (a == 1)
			cheat = N;
		else
			while (1) {
				int min;
				int ccount = count;
				for (int i = 0; i < N; i++) {
					if (b[i] >= a) {
						min = i;
						break;
					}
					if (i == N - 1 && b[i] < a)
						min = i + 1;
				}
				for (int i = 0; i < min; i++) {
					if (b[i] == 0)
						continue;
					a += b[i];
					b[i] = 0;
					count++;
				}
				if (ccount == count) { //cheat
					if (b[min] - a > a - 1) {
						b[min] = 0;
						count++;
					} else {
						a += (a - 1);
					}
					cheat++;
				}
				if (count == N)
					break;
			}
		cout << "Case #" << temp1 - T << ": " << cheat << endl;
	}
	return 0;
}
