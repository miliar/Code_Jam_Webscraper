#include <bits/stdc++.h>

using namespace std;

const int maxn = 1e9 + 10;



int main()
{
	int T;
	cin >> T;
	int cas = 0;
	while (T--)
	{
		cout << "Case #" << ++cas << ": ";
		int n;
		cin >> n;
		if (n == 0)
		{
			cout << "INSOMNIA\n";
			continue;
		}
		bool b[11];
		memset(b, 0, sizeof(b));
		for (int i = 1; ; ++i)
		{
			int p = n * i;
			while (p)
			{
				b[p % 10] = 1;
				p /= 10;
			}
			int sum = 0;
			for (int j = 0; j < 10; ++j)
			{
				sum += b[j];
			}
			if (sum == 10)
			{
				cout << n * i << endl;
				break;
			}
		}
	}

	return 0;
}