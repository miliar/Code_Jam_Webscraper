#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

int gao(int S, string audiences) {
	int sz = audiences.size();
	int sum = 0;
	int ans = 0;
	for (int i = 0; i < sz; i ++) {
		int number = audiences[i] - '0';
		if (sum < i) {
		//	cout << "i - sum = " << (i - sum) << "\n";
			ans += (i - sum);
			sum = i;
		}
		sum += number;
	}
	return ans;
}

int main(int argc, char const *argv[]) {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++) {
		int S;
		string audiences;
		cin >> S >> audiences;
		int ans = gao(S, audiences);
		cout << "Case #" << t << ": " << ans << "\n";
	}
	return 0;
}