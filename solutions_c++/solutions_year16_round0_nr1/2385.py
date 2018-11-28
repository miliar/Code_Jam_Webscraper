#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		int n;
		cin >> n;
		if (n == 0) {
			cout << "INSOMNIA\n";
			continue;
		}		
		set<char> se;
		int ans = 0;
		while (se.size() != 10) {
			ans += n;
			string s = to_string(ans);
			for (auto x: s)
				se.insert(x);
		}
		cout << ans << endl;
	}
}