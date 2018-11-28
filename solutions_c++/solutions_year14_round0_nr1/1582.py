#include <iostream>
using namespace std;

void solve(int c)
{
	cout << "Case #" << c << ": ";
	int x;
	bool f[17];
	for (int i = 0; i < 17; ++i) f[i] = false;
	cin >> x;
	for (int i = 1; i <= 4; ++i)
	{
		for (int j = 1; j <= 4; ++j)
		{
			int t;
			cin >> t;
			if (i == x) f[t] = true;
		}
	}
	cin >> x;
	int ans = 0;
	for (int i = 1; i <= 4; ++i)
	{
		for (int j = 1; j <= 4; ++j)
		{
			int t;
			cin >> t;
			if (i != x) continue;
			if (f[t])
			{
				if (ans == 0) ans = t;
				else
				{
					cout << "Bad magician!" << endl;
					x = 5;
				}
			}
		}
	}
	if (x == 5) return;
	if (ans == 0) cout << "Volunteer cheated!" << endl;
	else cout << ans << endl;
	return;
}

int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i)
	{
		solve(i);
	}
	return 0;
}
