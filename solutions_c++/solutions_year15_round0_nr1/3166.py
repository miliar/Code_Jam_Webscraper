#include <iostream>

using namespace std;

const int MAXN = 1010;

int ps[MAXN];

void solve(int testN) {
	int n;
	string s;
	cin >> n >> s;
	n++;
	for (int i = 0; i < n; i++)
		ps[i + 1] = ps[i] + s[i] - '0';
	int ans = 0;
	for (int i = 0; i < n; i++)
		ans = max(ans, i - ps[i]);
	cout << "Case #" << testN << ": " << ans << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i + 1);
	return 0;
}
