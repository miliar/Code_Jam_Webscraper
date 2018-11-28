#include <iostream>

using namespace std;

int main() {
	int T, A, B, K;
	cin >> T;
	for (int t = 0; t < T; t++) { 
		int result = 0;
		cin >> A >> B >> K;
		if (A > B) {
			int temp = A;
			A = B;
			B = temp;
		}				// A <= B
		if (K >= A) {
			result = A*B;
		}
		else {			// K < A <= B
			result += (K*B);
			result += (A-K)*K;
			for (int i = K; i < A; i++) {
				for (int j = K; j < B; j++)
					if ((i & j) < K)
						result++;
			}
		}
		cout << "Case #" << t+1 << ": " << result << endl;
	}
	return 0;
}
