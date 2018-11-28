#include <bits/stdc++.h>

using namespace std;

int main()
{
	size_t n; cin >> n;
	for (size_t i = 1; i <= n; ++i) {
		size_t k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << i << ":";
		for (size_t j = 1; j <= k; ++j)
			cout << " " << j;
		cout << endl;
	}
	return 0;
}
