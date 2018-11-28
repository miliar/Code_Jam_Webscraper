#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(void) {
	int n; cin >> n;

	for (int i = 0; i < n; i++) {
		ll a, ans = 0, v[11];
		cin >> a;
		if (a == 0) {
			cout << "Case #"<< i+1 <<": " << "INSOMNIA" << endl;
			continue;
		}

		memset(v, 0, sizeof(v));

		ll j = 1;
		while(true) {
			int b = a*j;
			ans = b;
			j++;

			while (b != 0) {
				int dig = b % 10;
				v[dig] = 1;
				b/=10;
			}

			bool flag = true;
			for (int k = 0; k <= 9; k++)
				if (v[k] == 0) flag = false;

			if (flag) break;
		}
		
		cout << "Case #"<< i+1 <<": " << ans << endl;
	}
}
