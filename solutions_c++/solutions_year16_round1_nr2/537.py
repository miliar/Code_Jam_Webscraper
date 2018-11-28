#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 2505;
int n, t;

int main() {
	ios_base::sync_with_stdio(0);
	ifstream cin("B.in");
	ofstream cout("B.out");
	cin >> t;
	for (int rep = 1; rep <= t; rep++) {
		cout << "CASE #" << rep << ":";
		int cnt[maxn];
		memset(cnt, 0, sizeof(cnt));
		cin >> n;
		for (int i = 0; i < (2*n-1)*n; i++) {
			int k;
			cin >> k;
			cnt[k]++;
		}
		for (int i = 0; i < maxn; i++) {
			if (cnt[i]%2 == 1) cout << ' ' << i;
		}
		cout << '\n';
	}
	return 0;
}

