#include <iostream>
#include <string>
using namespace std;
int main() {
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	int n, k, people, sum;
	cin >> n;
	string g;
	for (int i = 1; i <= n; i++) {
		cin >> k >> g;
		people = 0;
		sum = 0;
		for (int j = 0; j < g.size(); j++) {
			if (sum < j) {
				people += j - sum;
				sum += j - sum;
			}
			sum += g[j] - '0';
		}
		cout << "Case #" << i << ":" << " " << people << endl;
	}
	return 0;
}