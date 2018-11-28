#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

int field[10][10];

bool xcheck(int M, int indi) {
	for (int i = 0; i < M; i++) {
		if (field[indi][i] != 1)
			return false;
	}
	return true;
}

bool ycheck(int N, int indj) {
	for (int i = 0; i < N; i++) {
		if (field[i][indj] != 1)
			return false;
	}
	return true;
}

int main() {
	int T, N, M;
	int counter = 1;
	int answer, index, indcount;
	cin >> T;
	while (T-- > 0) {
		cin >> N >> M;
		answer = 1;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cin >> field[i][j];
			}
		}
		
		if (N == 1 || M == 1)
			answer = 1;
		else {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (field[i][j] == 1) {
						if (!xcheck(M, i) && !ycheck(N, j))
							answer = 0;
					}
				}
			}
		}
		
		if (answer == 1)
			cout << "Case #" << counter << ": YES" << endl;
		else
			cout << "Case #" << counter << ": NO" << endl;
		counter++;
	}
	return 0;
}