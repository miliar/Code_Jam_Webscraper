#include <iostream>
#define MAX 1010
using namespace std;

int main() {
	int T, k, arr[MAX];
	string str;

	cin >> T;

	for (int t=1 ; t<=T ; ++t) {
		cin >> str >> k;

		int len = str.length();

		for (int i=0 ; i<len ; ++i)
			arr[i] = 0;

		int curr = 0, ans = 0;
		for (int i=0 ; i<len ; ++i) {
			if ((str[i] == '-' && curr == 0) || (str[i] == '+' && curr == 1)) {
				arr[i] ^= 1;
				arr[i+k-1] ^= 1;
				ans++;
				if (i + k > len) {
					ans = -1;
					break;
				}
			}
			curr ^= arr[i];
		}
		cout << "Case #" << t << ": ";
		if (ans == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << endl;
	}
}