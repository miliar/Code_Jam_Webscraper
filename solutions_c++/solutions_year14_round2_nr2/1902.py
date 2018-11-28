#include <iostream>

using namespace std;

int main(){

	int T; cin >> T;
	for (int tst = 1; tst <= T; tst++){
		int A, B, K; cin >> A >> B >> K;
		int ans = 0;
		for (int i = 0; i < A; i++){
			for (int j = 0; j < B; j++){
				int C = i & j;
				if (C < K) {
					ans++;
				}
			}
		}
		cout << "Case #" << tst << ": " << ans << endl;
	}
	return 0;
}