#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int num[2000];

int main() {
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		int N;
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> num[i];
		}
		int l = 0;
		int r = N - 1;
		int cost = 0;
		while (l < r) {
			int mini = l;
			for (int i = l; i <= r; i++){
				if (num[i] < num[mini]) {
					mini = i;
				}
			}
			if (mini - l < r - mini) {
				cost += mini - l;
				for (int i = mini; i > l; i--) {
					num[i] = num[i - 1];
				}
				l++;
			}
			else {
				cost += r - mini;
				for (int i = mini; i <= r; i++) {
					num[i] = num[i + 1];
				}
				r--;
			}
		}
		cout << "Case #" << c << ": " << cost << endl;
	}
	return 0;
}