#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

#define FILE "A"

int main() {
	ios_base::sync_with_stdio(false);
	freopen(FILE ".in", "r", stdin);
	freopen(FILE ".out", "w", stdout);
	int T;
	cin >> T;
	for (int _ = 0; _ < T; ++_) {

		int N;
		cin >> N;
		string s;
		cin >> s;
		int A[N + 1];
		for (int i = 0; i <= N; ++i) {
			A[i] = s[i] - '0';
		}
		int sum = A[0];
		int ans = 0;
		for (int i = 1; i <= N; ++i) {
			ans = max(ans, i - sum);
			sum += A[i];
		}		
		/*
			Print answer
		 */
		cout << "Case #" << _+1 << ": ";
		cout << ans;
		cout << "\n";
	}
	return 0;
}