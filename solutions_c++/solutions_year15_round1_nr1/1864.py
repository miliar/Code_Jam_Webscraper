#include <iostream>
#include <vector>

using namespace std;

int main () {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N;
		cin >> N;
		vector<int> M;
		for (int n = 0; n < N; ++n) {
			int mi;
			cin >> mi;
			M.push_back(mi);
		}

		int y = 0;
		for (int i = 1; i < N; ++i) {
			if (M[i] < M[i-1]) {
				y += M[i-1] - M[i];
			}
		}

		int maxd = 0;
		for (int i = 1; i < N; ++i) {
			if (M[i-1] - M[i] > maxd) maxd = M[i-1] - M[i];
		}

		int z = 0;
		for (int i = 0; i < N-1; ++i) {
			if (M[i] > maxd) {
				z += maxd;
			} else {
				z += M[i];
			}
		}

		cout << "Case #" << t << ": " << y << " " << z << endl;
	}
	return 0;
}
