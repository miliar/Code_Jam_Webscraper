#include <bits/stdc++.h>

using namespace std;

const int BITSET_SIZE = 14;

long long get_base_no(const string& s, int base)
{
	long long ans = 0;
	long long wt = 1;
	for (int i = s.length() - 1; i >= 0; i--) {
		ans += (s[i] - '0') * wt;
		wt *= base;
	}
	return ans;
}

long long get_div(long long n)
{
	for (long long i = 2; i * i <= n; i++) {
		if (n % i == 0) {
			return i;
		}
	}
	return 0;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int n, j;
		cin >> n >> j;
		cout << "Case #" << i << ":\n";
		int count = 0;
		for (unsigned i = 0; i < 1u << (n - 2); i++) {
			bitset<BITSET_SIZE> b(i);
			string s = '1' + b.to_string() + '1';
			vector<long long> divs;
			for (int j = 2; j <= 10; j++) {
				long long div;
				if ((div = get_div(get_base_no(s, j))) == 0) {
					break;
				}
				divs.push_back(div);
			}
			if (divs.size() == 9) {
				cout << s << ' ';
				for (auto div: divs) {
					cout << div << ' ';
				}
				cout << '\n';
				count++;
			}
			if (count == j) {
				break;
			}
		}
	}
	return 0;
}
