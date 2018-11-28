#include <iostream>
#include <vector>

using namespace std;

string calculate(int N, int M, vector<int> a) {
	vector<int> r, c; // min values
	int i, j, x;
	r.reserve(M);
	c.reserve(N);

	for (j = 0; j < M; ++j) {
		r[j] = 0;
	}

	for (i = 0; i < N; ++i) {
		c[i] = 0;
		for (j = 0; j < M; ++j) {
			x = i*M+j;
			if (a[x] > r[j]) {
				r[j] = a[x];
			}

			if (a[x] > c[i]) {
				c[i] = a[x];
			}
		}
	}

	// let's check it now
	for (i = 0; i < N; ++i) {
		for (j = 0; j < M; ++j) {
			x = i*M+j;
			if (a[x] < r[j] && a[x] < c[i]) {
				return "NO";
			}
		}
	}
	return "YES";
}

int main() {
	int T, N, M;
	int i, j, t;
	vector<int> a;

	cin >> T;

	for (i = 1;  i <= T; ++i) {
		a.clear();
		cin >> N >> M;
		j = N * M;
		while (j > 0) {
			cin >> t;
			a.push_back(t);
			--j;
		}
		cout << "Case #" << i << ": " << calculate(N, M, a) << endl;
	}
}
