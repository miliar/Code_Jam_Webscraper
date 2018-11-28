#include <bits/stdc++.h>

using namespace std;


int main()
{
	int T;
	cin >> T;
	int cas = 0;
	while (T--)
	{
		cout << "Case #" << ++cas << ":";
		int k, c, s;
		cin >> k >> c >> s;
		long long sum = 1ll;
		for (int i = 1; i < c; ++i)
		{
			sum *= k;
		}
		for (int i = 1; i <= k; ++i)
		{
			cout << " " << sum * i;
		}
		cout << endl;
	}



	return 0;
}