#include <iostream>

using namespace std;

int T, K, C, S, cases = 1;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	while (cases <= T)
	{
		cin >> K >> C >> S;

		if (!(K < (C + S)))
		{
			cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
			cases++;
			continue;
		}

		if (S == 1)
		{
			cout << "Case #" << cases << ": " << K << endl;
			cases++;
			continue;
		}

		if (C == 1)
		{
			cout << "Case #" << cases << ":";

			for (int i = 1; i <= K; i++)
			{
				cout << " " << i;
			}

			cout << endl;
			cases++;
			continue;
		}

		cout << "Case #" << cases << ":";

		for (int i = K-1; S > 0; i++)
		{
			cout << " " << i;
			S--;
		}

		cout << endl;

		cases++;
	}

	return 0;
}