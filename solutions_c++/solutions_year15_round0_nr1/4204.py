#include <iostream>
#include <string.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	string str;

	for (int i = 0 ; i < T ; ++i) {
		int N;
		cin >> N;
		cin >> str;
		int ans = 0;
		int sum = 0;
		
		for (int j = 0 ; j < str.length() ; ++j) {
			int n = str[j] - '0';

			if (n != 0) {
				if (j > sum) {
					ans += (j - sum);
					sum = j+n;
				} else {
					sum += n;
				}
			}
		}

		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}