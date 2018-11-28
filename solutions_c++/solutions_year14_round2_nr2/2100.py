#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, a, b, k, idx = 1;
	long long res;
	cin >> t;
	while(t--) {
		res = 0;
		cin >> a >> b >> k;
		for(int i = 0; i < a; i++)
			for(int j = 0; j < b; j++)
				if((i & j) < k) res++;
		cout << "Case #" << idx++ << ": " << res << endl;
	}

	return 0;
}
