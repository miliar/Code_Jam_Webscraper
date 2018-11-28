#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	n = (n-4)/2;
	cout << "Case #1:\n";
	for(int i = 0; i < k; i++) {
		string s = "";
		for(int j = 0; j < n; j++) s += (i & (1<<j) ? "11" : "00");
		cout << "11" << s << "11 ";
		for(int d = 2; d <= 10; d++) cout << d+1 << " ";
		cout << "\n";
	}
	return 0;
}
