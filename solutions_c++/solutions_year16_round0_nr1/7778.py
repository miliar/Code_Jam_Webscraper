#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		bool mark[10];
		for (int i = 0; i < 10; i++)
			mark[i] = 0;
		int n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << t << ": INSOMNIA" << endl;
			continue;
		}
		bool f = 1;
		long long i;
		for (i = n; f; i += n) {
			long long j = i;
			while (j > 0) {
				mark[j % 10] = 1;
				j /= 10;
			}
			f = 0;
			for (int i = 0; i < 10; i++)
				if (!mark[i]) {
					f  = 1;	  
					break;
				}
		}
		cout << "Case #" << t << ": " << i-n << endl;
	}
	return 0;
}
