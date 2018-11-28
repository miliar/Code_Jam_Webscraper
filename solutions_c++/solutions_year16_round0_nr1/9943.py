#include <iostream>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long int N;
		cin >> N;
		bool digit[10] = {};

		long long int ans = -1;

		for (int i = 1; i < 100000; i++) {
			long long int CN = N * i;
			long long int TN = CN;
			
			int r = CN;
			if (CN == 0 || i == 100000-1){
				ans = -1;
				break;
			}

			while (CN != 0) {
				long long int r = CN % 10;
				CN = CN / 10;
			
				digit[r] = true;
				
			}
			bool mfinish = true;
			for (int j = 0; j < 10; j++) {
				if (digit[j] == false) {

					mfinish = false;
					break;
				}
			}
			if (mfinish) {
				ans = TN;
				break;
			}

		}

		if (ans == -1) {
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << t << ": " << ans << endl;
		}

	}
	return 0;
}