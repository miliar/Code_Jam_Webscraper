#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
ll pw(ll b, ll p) { if (!p) return 1; ll sq = pw(b, p / 2); sq *= sq; if (p % 2) sq *= b; return sq; }

int maxValue, s, cnt;
string x, keys, target;

void solve(int K, int L)
{
	if (x.length() == s)
	{
		int temp = 0;

		for (int i = 0; i < s; ++i)
		{
			if (x.substr(i, L) == target)
			{
				++cnt;
				++temp;
			}
		}

		maxValue = max(maxValue, temp);
	}
	else
	{
		for (int i = 0; i < K; ++i)
		{
			x += keys[i];
			solve(K, L);
			x.pop_back();
		}
	}
}

int main()
{
	freopen("B-input.txt", "r", stdin);
	freopen("B-output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int K, L;
		cin >> K >> L >> s >> keys >> target;
		cnt = maxValue = 0;
		int tot = pw(K, s);
		solve(K, L);

		double result = maxValue - double(cnt) / tot;
		cout << fixed << setprecision(7);
		cout << "Case #" << t << ": " << result << "\n";
	}
}
