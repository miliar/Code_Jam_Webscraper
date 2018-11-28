#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <iostream>


#define max(a, b) (a > b ? a : b)

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		int Smax;
		cin >> Smax;

		int t = 0, answer = 0;
		for (int j = 0; j <= Smax; ++j)
		{
			int delta = max(0, j - t);
			answer += delta;

			char c;
			cin >> c;
			t += c - '0' + delta;
		}

		cout << "Case #" << i + 1 << ": " << answer << endl;
	}

	return 0;
}
