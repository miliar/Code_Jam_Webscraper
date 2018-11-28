#include <bits/stdc++.h>
using namespace std;

void solve(){
	long long n;
	cin >> n;

	if (n == 0) {
		cout << "INSOMNIA";
		return;
	}

	long long cur = n;
	int a[10] = {0};
	for (int i = 1; ; i++, cur += n) {
		int tmp = cur;
		while (tmp > 0) {
			a[tmp % 10] = 1;
			tmp /= 10;
		}
		bool can = true;
		for (int j = 0; j < 10; j++) {
			if (a[j] == 0) {
				can = false;
			}
		}
		if (can) {
			cout << cur;
			return;
		}
	}
}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
