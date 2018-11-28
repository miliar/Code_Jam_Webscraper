#include <iostream>
#include <algorithm>

using namespace std;

int d[10001];

int main() {
	int t;
	cin >> t;
	for (int cn=1; cn<=t; cn++) {
		cout << "Case #" << cn << ": ";
		int n, x;
		cin >> n >> x;
		for (int i=0; i<n; i++) cin >> d[i];
		sort(d, d+n, greater<int>());
		int s = 0;
		for (int i=0; i<n; i++) {
			s++;
			if (i == n-1) break;
			if (d[i] + d[n-1] <= x) n--;
		}
		cout << s << "\n";
	}
	return 0;
}