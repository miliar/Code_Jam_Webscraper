#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	int T, A, N; cin >> T;
	vector<int> vres(T);

	for (int i = 0; i < T; i++) {
		cin >> A >> N;
		vector<int> vi(N);
		for (int j = 0; j < N; j++) cin >> vi[j];

		sort(vi.begin(), vi.end());

		int res = 101;
		for (int j = 0; j <= 100; j++) {
			int rest = j;
			int B = A;

			int p = 0;
			while (1) {
				if (p == N) break;

				if (vi[p] < B) {
					B += vi[p];
					p++;
				} else if (rest > 0) {
					B = 2*B-1;
					rest--;
				} else {
					break;
				}
			}

			res = min(res, N-p+j);
		}
		vres[i] = res;
	}

	ofstream ofs("output.txt");
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i+1 << ": " << vres[i] << endl;
		ofs << "Case #" << i+1 << ": " << vres[i] << endl;
	}
	return 0;
}
