#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <queue>

using namespace std;

int main()
{
	int T;
	cin >> T;

	int R, N, M, K;
	cin >> R >> N >> M >> K;

	cout << "Case #1:" << endl;

	for (int r = 0; r < R; r++)
	{
		int input;
		int n = N;
		map<int, int> guess;
		vector<int> real_guess;

		for (int k = 0; k < K; k++)
		{
			cin >> input;
			int temp = input;
			int tempN = N;
			vector<int> temp_guess;

			if (input == 1)
			{
			}
			else
			{
				for (int m = M; m >= 2 && n > 0; m--)
				{
					if ((input % m == 0))
					{
						if (temp == 1)
						{
							temp = input;
							tempN = N;
						}
						while (temp % m == 0)
						{
							temp /= m;
							guess[m]++;
							tempN--;
							temp_guess.push_back(m);
						}

						if (tempN == 0)
						{
							real_guess = temp_guess;
							n = 0;
						}
					}
				}
			}
		}

		if (real_guess.size() > 0)
		{
			for (int i = 0; i < real_guess.size(); i++)
				cout << real_guess[i];
		}
		else if (guess.size() == 0)
		{
			for (int i = 2; i <= M && i <= N + 1; i++)
			{
				for (int j = i; j <= N + 1; j += M - 1)
					cout << i;
			}
		}
		else
		{
			int guess_num = 0;
			while (guess_num < N)
			{
				int max = 0;
				int max_num = 0;
				// Iterate through the map
				for (map<int, int>::iterator it = guess.begin();
					it != guess.end(); ++it)
				{
					if (max < it->second)
					{
						max = it->second;
						max_num = it->first;
					}
				}
				cout << max_num;
				guess[max_num]--;
				guess_num++;
			}
		}

		cout << endl;
	}

	return 0;
}
