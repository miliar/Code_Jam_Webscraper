//In the name of God
#include <algorithm>
#include <iostream>
using namespace std;
const int N = 1000 + 100, oo = 1e9;


int a[N], adr[N], b[N], n;

int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i], b[i] = a[i];
		sort(b, b + n);
		for (int i = 0; i < n; i++)
			adr[a[i] = lower_bound(b, b + n, a[i]) - b] = i;
		for (int i = 0; i < n; i++)
			b[i] = i;
		int ans = oo;
		do {
			int mx = max_element(b, b + n) - b;
			bool flag = false;
			for (int i = 0; i < mx - 1; i++)
				if (b[i] > b[i + 1])
					flag = true;
			if (flag)
				continue;
			for (int i = mx; i < n - 1; i++)
				if (b[i] < b[i + 1])
					flag = true;
			if (flag)
				continue;
			int tmp = 0;
			for (int i = 0; i < n; i++)
				for (int j = 0; j < i; j++)
					if (adr[b[j]] > adr[b[i]])
						tmp++;
			ans = min(ans, tmp);
		} while (next_permutation(b, b + n));
		cout << "Case #" << test << ": " << ans << '\n';
	}
	return 0;
}

