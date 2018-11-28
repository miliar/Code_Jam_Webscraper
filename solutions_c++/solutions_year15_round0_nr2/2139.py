#include <iostream>
#include <algorithm>

using namespace std;

#define MAXN 1005

int solve(int test) {
	int n;
	int a[MAXN];

	cin >> n;
	int last = 0;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		last = max(last, a[i]);
	}
	
	int result = last;

	for (int t = 1; t <= last; t++) {
		int count = 0;
		for (int i = 0; i < n; i++) 
			count += (a[i]-1)/t;
		count += t;
		result = min(result, count);
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
