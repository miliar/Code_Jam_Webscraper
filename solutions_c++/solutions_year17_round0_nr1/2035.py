#include <iostream>
#include <string>

using namespace std;

string S;
int K;

inline void init()
{
	cin >> S;
	cin >> K;
}

inline void solve()
{
	int i, j;
	int rval = 0;

	for (i = 0; i + K - 1 < S.size(); i++)
		if (S[i] == '-')
		{
			rval++;
			for (j = 0; j < K; j++)
				switch (S[i + j])
				{
				case '+':
					S[i + j] = '-';
					break;
				case '-':
					S[i + j] = '+';
				}
		}

	for (i = 0; i < S.size(); i++)
		if (S[i] == '-')
		{
			cout << "IMPOSSIBLE\n";
			return;
		}

	cout << rval << "\n";
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);

	int T, i;

	cin >> T;

	for (i = 1; i <= T; i++)
	{
		init();
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}