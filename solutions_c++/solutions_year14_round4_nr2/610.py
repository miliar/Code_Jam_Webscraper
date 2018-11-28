#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

int T, n, num[1024], lft[1024], rght[1024], bit[1024], srt[1024];

int query(int x)
{
	int ans = 0;
	while (x) {
		ans += bit[x];
		x -= x & -x;
	}
	return ans;
}

void update(int x)
{
	while (x < 1024)
	{
		bit[x]++;
		x += x & -x;
	}
}

int main()
{
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		for (int i = 0; i < 1024; i++) bit[i] = 0;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> num[i];
			srt[i] = num[i];
		}
		sort(srt, srt + n);
		map<int, int> cor;
		for (int i = 0; i < n; i++)
		{
			cor[srt[i]] = i + 1;
		}
		for (int i = 0; i < n; i++) num[i] = cor[num[i]];


		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			lft[i] = i - query(num[i]);
			update(num[i]);
		}
		for (int i = 0; i < 1024; i++) bit[i] = 0;

		for (int i = n - 1; i + 1; i--)
		{
			rght[i] = n - 1 - i - query(num[i]);
			update(num[i]);
		}
		for (int i = 0; i < n; i++) ans += min(lft[i], rght[i]);
		cout << "Case #" << C << ": " << ans << '\n';
	}
	return 0;
}

