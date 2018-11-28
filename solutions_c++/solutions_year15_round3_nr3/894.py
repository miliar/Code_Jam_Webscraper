#include<iostream>
#include<utility>
#include<vector>
#include<string>
using namespace std;

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int t, it, i, c, d, v, dp[200], x, j, ans;
	vector<int> input;
	int possible[200];
	cin >> t;
	for (it = 1; it <= t; it++) {
		cin >> c >> d >> v;
		input.clear();
		for (i = 1; i <= v; i++) {
			dp[i] = 0;
			possible[i] = 1;
		}
		for (i = 0; i < d; i++) {
			cin >> x;
			input.push_back(x);
		}
		for (i = 0; i < d; i++) {
			x = input[i];
			for (j = v; j > x; j--) {
				dp[j] = dp[j-x];
			}
			dp[x] = 1;
		}
		ans = 0;
		for (i = 1; i <= v; i++) {
			if (dp[i] == 0) {
				// cannot pay a product with value i
				possible[i] = 0;
			} else {
		//		cout << i << " ";
			}
		}
		
		for (i = 1; i <= v; i++) {
			if (possible[i] == 0) {
				// this will be a new coin
				ans++;
				for (j = v; j >= i+1; j--) {
					if (possible[j - i] == 1) {
						possible[j] = 1;
			//			cout << j << " becomes possible with coin " << i << endl;
					}
				}
			//	cout << "I need " << i << endl;
				possible[i] = 1;
			}
		}
		cout << "Case #" << it << ": " << ans << "\n";
	}
	return 0;
}