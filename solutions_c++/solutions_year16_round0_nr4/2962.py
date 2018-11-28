#include <bits/stdc++.h>

using namespace std;

int main() {
	long long int T;
	cin >> T;
	
	for (long long int e = 0; e < T; e++) {
		long long int C, K, S;
		cin >> K >> C >> S;
		long long int answer = -1;
		cout << "Case #" << e + 1 << ": ";
		if (K == S) {
			for (int i = 0; i < S; i++) {
				long long int n = pow(K, C);
				long long int answer = 0;
				long long int nn = 0;
				while (n > K) {
					n /= K;
					nn += nn * i;
				}
				answer = nn + i;
				
				cout << answer + 1 << " ";
			}
			cout << "\n";
		}
		else {
			cout << "IMPOSSIBLE\n";
		}
		
	}
	
	return 0;
} 
