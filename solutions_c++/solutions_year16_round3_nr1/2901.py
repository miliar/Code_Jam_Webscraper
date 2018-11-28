// a.cpp

#include <algorithm>
#include <iostream>

using namespace std;

int findLastRemove(int* parties, int N, int all) {
	for (int i = 0; i < N; ++i) {
		// if remove i
		parties[i] --;
		all --;

		int* idx = max_element(parties, parties+N);
		if (*idx * 2 <= all) {
			return i;
		} else {
			parties[i] ++;
			all ++;
		}
	}
	return -1;
}

int main() {

	int T;
	cin >> T;

	for (int i = 0; i < T; ++i) {
		int N;
		cin >> N;
		int parties[N] = {0};
		int all = 0;
		for (int j = 0; j < N; ++j) {
			cin >> parties[j];
			all += parties[j];
		}

		cout << "Case #" << i+1 << ": ";

		while (all > 0) {
			if (2 == all) {
				for (int j = 0; j < N; ++j) {
					if (1 == parties[j]) {
						cout << char('A'+j);
					}
				}
				all = 0;
				cout << endl;
				break;
			}

			int* idx = max_element(parties, parties+N);
			int firstRemove = idx - parties;
			all --;
			parties[firstRemove] --;

			cout << char('A' + firstRemove);
			int lastRemove = findLastRemove(parties, N, all);
			if (lastRemove != -1) {
				all --;
				cout << char('A' + lastRemove);
			}
			cout << " ";
		}
		
	}

	return 0;
}