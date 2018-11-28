#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, cas = 0;
	long long n;
	cin >> t;
	while (t-- && cin >> n) {
		bool flag[10] = {0};
		int cot = 0;
		cout << "Case #" << ++cas << ": ";
		if (n) {
			for (long long i = 1; ; ++i) {
				long long cur = i * n;
				while (cur) {
					if (flag[cur % 10] == 0) {
						++cot;
						flag[cur % 10] = 1;
					}
					cur /= 10;
				}
				if (cot == 10) {
					cout << i * n <<endl;
					break;
				}
			}
		}
		else {
			cout << "INSOMNIA" << endl;
		}
	}
	return 0;
}
