#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int step (int A, int n, int N, vector<int> m, int op) {
	//cout << "A :" << A << ", n: " << n << ", op:" << op << endl;
	if (n >= N) return op;
	if (m[n] < A) {
		return step(A+m[n], n+1, N, m, op);
	}
	else {
		int way2 = step(A, n+1, N, m, op+1);
		if (A-1 == 0) return way2;
		int way1 = step(A*2-1, n, N, m, op+1);
		return (way1 < way2)? way1 : way2;
	}
}

int main () {
	int T, A, N;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> A;
		cin >> N;
		vector <int> m (N);
		for (int n = 0; n < N; ++n){
			cin >> m[n];
		}
		sort(m.begin(), m.end());
		cout << "Case #" << t+1 << ": " << step(A, 0, N, m, 0) << endl;
	}
}