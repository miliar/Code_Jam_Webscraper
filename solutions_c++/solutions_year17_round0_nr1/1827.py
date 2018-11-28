#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <ctime>
using namespace std;

void solve()
{
	int k;
	string s;

	cin >> s;
	cin >> k;
	int ans = 0;
	for (int i = 0; i <= s.size()-k; ++i)
	{
		if (s[i] == '-') {
			++ans;
			for (int j = 0; j < k; ++j)
			{
				s[i + j] = (s[i + j] == '-') ? '+' : '-';
			}
		}
	}
	for (int i = s.size() - k + 1; i < s.size(); ++i)
	{
		if (s[i] == '-') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << ans << endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		clock_t start = clock();
		printf("Case #%d: ", test);
		solve();
		clock_t finish = clock();
		cerr << "Test" << test << ": " << (finish - start + .0) / CLOCKS_PER_SEC << endl;
	}
	

	return 0;
}