#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		long long n;
		cin >> n;
		bool is_present[10] = { false };
		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA\n";
			continue;
		}
		int curr = n;
		while (true) {
			string number = to_string(curr);
			for (char c: number) {
				is_present[c - '0'] = true;
			}
			if (find(begin(is_present), end(is_present), false) ==
					is_present + 10) {
				break;
			}
			curr += n;
		}
		cout << "Case #" << i << ": " << curr << '\n'; 
	}
	return 0;
}
