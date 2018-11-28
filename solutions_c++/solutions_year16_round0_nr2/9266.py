#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <string>

using namespace std;

int T;
string A;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> A;
		
		int ans = 0;
		for (int i = 1; i < A.size(); i++) {
			if (A[i] != A[i - 1]) ans++;
		}

		ans += (A[0] == '-') ^ (ans % 2);

		printf("Case #%d: %d\n", t, ans);
	}
}
