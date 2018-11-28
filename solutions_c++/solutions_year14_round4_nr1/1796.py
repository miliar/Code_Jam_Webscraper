
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N, size;
		cin >> N >> size;

		int s[N];

		for (int i = 0; i < N; i++) cin >> s[i];
		sort(s, s+N);

		int count = 0;
		for (int big = N-1; big >= 0; big--)
		{
			//cout << "big = " << big << ", s[big] = " << s[big] << endl;
			if (s[big] < 0) continue;
			for (int small = big-1; small >= 0; small--)
			{
				if (s[small] < 0) continue;
				if (s[big] + s[small] <= size)
				{
					count++;
					//cout << "putting " << s[big] << ' ' << s[small] << endl;
					s[big] = -1;
					s[small] = -1;
					break;
				}
			}

			if (s[big] >= 0)
			{
				//cout << "putting " << s[big] << endl;
				count++;
				s[big] = -1;
			}
		}

		cout << "Case #" << t << ": " << count << endl;
	}

	return 0;
}
