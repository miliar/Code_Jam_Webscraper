#include <algorithm>
#include <iostream>
using namespace std;

typedef unsigned long long ULL;

int main() {
	int T,A,B,K;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> A >> B >> K;
		ULL ans = 0;
		for (int a = 0; a < A; a++) {
			for (int b = 0; b < B; b++) {
				if ((a&b)<K) ans++;
			}
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
}
