#include<iostream>
#include <vector>
using namespace std;

int main() {
	int T, N;
	vector<int> A;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> N;
		A.resize(N);
		for(int i = 0; i < N; ++i) cin >> A[i];
		int min_rate = 0;
		int m1 = 0, m2 = 0;
		for(int i = 1; i < N; ++i) {
			min_rate = max(min_rate, max(0, A[i - 1] - A[i]));
			m1 += max(0, A[i - 1] - A[i]);
		}
		for(int i = 0; i + 1 < N; ++i) {
			m2 += min(min_rate, A[i]);
		}
		cout << "Case #" << t << ": " << m1 << " " << m2 << endl;
		
	}
}
