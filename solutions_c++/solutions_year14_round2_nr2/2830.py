#include <iostream>

using namespace std;

int main(void) {
	long long A, B, K;
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> A >> B >> K;
		long long win = 0;
		for(int j = 0; j < A; j++)
			for(int k = 0; k < B; k++) {
				if(int(j&k) < K)
					win++;
			}
		cout << "Case #" << i << ": " << win << endl;
	}
	return 0;
}