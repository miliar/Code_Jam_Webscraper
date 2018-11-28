#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("/mnt/S/Code/in.txt", "rt", stdin);
	freopen("/mnt/S/Code/out.txt", "wt", stdout);


	int n, max, stand, ans;
	string s;
	cin >> n;



	for (int i = 0; i < n; ++i)
	{
		ans = 0;
		cin >> max;
		cin >> s;
		vector<int>v;
		for (int j = 0; j < s.length(); ++j)
		{
			v.push_back(s[j] - 48);
		}
		stand = v[0];
		for (int j = 1; j < max + 1; ++j)
		{
			if (stand < j) {
				ans += j - stand;
				stand += j - stand;
			}
			stand += v[j];
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}
