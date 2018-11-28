#include <bits/stdc++.h>

using namespace std;

size_t solve(const string & s)
{
	size_t n = s.size(), m = 0; vector<bool> v(n);
	for (size_t i = 0; i < n; ++i)
		v[i] = s[n - i - 1] == '+';
	auto flip = [&](size_t i) {
		if (i < n) {
			reverse(v.begin() + i, v.end());
			for (; i < n; ++i)
				v[i] = !v[i];
			++m;
		}		
	};
	for (size_t i = 0; i < n; ++i) {
		if (!v[i]) {
			size_t j = n;
			while (j >= i + 1 && v[j - 1])
				--j;
			flip(j);
			flip(i);
		}
	}
	return m;
}

int main()
{
	size_t n; cin >> n;
	for (size_t i = 0; i < n; ++i) {
		string s; cin >> s;
		cout << "Case #" << (i + 1) << ": " << solve(s) << endl;
	}
	return 0;
}
