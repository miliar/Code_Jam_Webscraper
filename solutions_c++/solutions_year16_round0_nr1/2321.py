#include<iostream>
#include<vector>
#include<cstdio>
#include<cmath>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<queue>

using namespace std;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	cin >> t;
	int done = 0;
	while (done<t) {
		long long n;
		cin >> n;
		long long ans = 0;
		if (n != 0) {
			int set = 0;
			while (set != ((1 << 10) - 1)) {
				ans = ans + n;
				long long temp = ans;
				while (temp > 0) {
					int dig = (int)(temp % (long long)10);
					set = set | (1 << dig);
					temp = temp / 10;
				}
			}
		}
		++done;
		cout << "Case #" << done << ": ";
		if (n == 0) cout << "INSOMNIA";
		else cout << ans;
		cout << endl;
	}
	return 0;
}