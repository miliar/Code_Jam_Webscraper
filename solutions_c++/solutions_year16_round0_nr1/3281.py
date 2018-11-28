#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>

using namespace std;

set<int> digits(long long N)
{
	int digit;
	set<int> dgts;

	while (N > 0)
	{
		digit = N % 10;
		N = (N - digit) / 10;

		dgts.insert(digit);
	}

	return dgts;
}

int main()
{
	int T, N;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		long long multiple;
		bool sleep = false;
		
		cin >> N;

		if (N == 0) cout << "Case #" << t << ": INSOMNIA" << endl;

		else
		{
			set<int> dgts, currDgts;

			for (multiple = N; multiple < LLONG_MAX; multiple += N)
			{
				currDgts = digits(multiple);
				dgts.insert(currDgts.begin(), currDgts.end());

				if (dgts.size() == 10) { sleep = true;  break; }
			}

			if (sleep) cout << "Case #" << t << ": " << multiple << endl;
			else cout << "Case #" << t << ": INSOMNIA" << endl;
		}
	}

	return 0;
}

#endif