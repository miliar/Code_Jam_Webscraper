//In the name of God
//...
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int test; cin >> test;
	for (int num = 1; num <= test; num++) {
		int mx; cin >> mx;
		vector<int> v;
		for (int i = 0; i <= mx; i++) {
			char c; cin >> c;
			while (c-- > '0') {
				v.push_back(i);
			}
		}
		int ans = 0;
		for (int i = 0; i < (int) v.size(); i++)
			ans = max(ans, v[i] - i);
		cout << "Case #" << num << ": ";
		cout << ans << '\n';
	}
	return 0;
}
