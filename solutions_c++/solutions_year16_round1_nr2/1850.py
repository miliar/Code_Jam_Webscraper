#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
	int t, n, x;
	cin >> t;
	vector<int>h(2505, 0);
	for(int l = 1; l <= t; l++) {
		cin >> n;
		for(int i = 0; i < 2 * n - 1; i++) {
			for(int j = 0; j < n; j++) {
				cin >> x;
				h[x]++;
			}
		}
		cout << "Case #" << l << ": ";
		int m = 1;
		for(; m < 2501; m++) {
			if(h[m] % 2 == 1) {
				cout << m;
				h[m] = 0;
				break;
			}
			h[m] = 0;
		}
		for(m = m + 1; m < 2501; m++) {
			if(h[m] % 2 == 1)
				cout << " " << m;
			h[m] = 0;
		}
		cout << endl;
	}
	return 0;
}