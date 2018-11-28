
#include <iostream>

int CountingSheep(int n)
{
	const int D = 10;
	int digitPresented[D];
	for (int i = 0; i < D; ++i)
	{
		digitPresented[i] = 0;
	}
	int nDigit = 0;

	for (int nn = n; ; nn += n)
	{
		int x = nn;
		while (x)
		{
			int m = x % D;
			if (!digitPresented[m])
			{
				++digitPresented[m];
				if (++nDigit == D)
				{
					return nn;
				}
			}
			x /= D;
		}
	}
}

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int N;
		cin >> N;

		if (N)
		{
			int ans = CountingSheep(N);
			cout << "Case #" << i << ": " << ans << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
	}

	return 0;
}
