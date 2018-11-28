#include <iostream>

using namespace std;

#define MAXN 1005

int solve(int test) {
	int n;
	cin >> n;
	char c;
	int a[MAXN];
	for (int i = 0; i <= n; i++) {
		cin >> c;
		a[i] = int(c) - int('0');
	}

	int result = 0;
	int count = 0;
	for (int i = 0; i <= n; i++) {
		if (count < i) {
			result += i-count;
			count += i-count+a[i];
		} else {
			count += a[i];
		}
	}
	
	cout << "Case #" << test << ": " << result << endl;

	return 0;
}

int main() {
	int test;
	cin >> test;

	for (int t = 0; t < test; t++) {
		solve(t+1);
	}
	
	return 0;
}
