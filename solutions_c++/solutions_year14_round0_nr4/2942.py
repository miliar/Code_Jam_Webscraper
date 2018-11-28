#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++ i) {
		int n;
		cin >> n;
		double w1[n], w2[n];
		for(int j = 0; j < n; ++ j)
			cin >> w1[j];
		sort(w1, w1 + n);
		for(int j = 0; j < n; ++ j)
			cin >> w2[j];
		sort(w2, w2 + n);
		int ans = 0;
		int l1 = 0, r1 = n - 1, l2 = 0, r2 = n - 1;
		for(int j = 0; j < n; ++ j) {
			if(w1[l1] < w2[l2]) {
				++ l1;
				-- r2;
			}
			else {
				++ l1;
				++ l2;
				++ ans;
			}
		}
		cout << "Case #" << i + 1 << ": " << ans << " ";
		ans = 0;
		l1 = 0, r1 = n - 1, l2 = 0, r2 = n - 1;
		for(int j = 0; j < n; ++ j)
			if(w1[l1] < w2[l2]) {
				++ l1;
				++ l2;
			}
			else {
				-- r1;
				++ l2;
				++ ans;
			}
		cout << ans << endl;
	}
}