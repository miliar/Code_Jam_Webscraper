#include <iostream>

using namespace std;

int main()
{
	int n, T;
	double a[2000], b[2000], used[2000];
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		for (int i = 0; i < n; i++)
			cin >> b[i];
		memset(used, 0, sizeof used);
		int score = 0;
		for (int i = 0; i < n; i++)
		{
			double m = 1.0;
			int k = -1;
			for (int j = 0; j < n; j++)
			{
				if (m > a[j] && a[j] > b[i] && !used[j])
				{
					m = a[j];
					k = j;
				}
			}
			if (k == -1)
			{
				for (int j = 0; j < n; j++)
				{
					if (m > a[j] && !used[j])
					{
						m = a[j];
						k = j;
					}
				}
				used[k] = 1;
			}
			else
			{
				used[k] = 1;
				score++;
			}
		}
		cout << score << ' ';
		memset(used, 0, sizeof used);
		score = 0;
		for (int i = 0; i < n; i++)
		{
			double m = 1.0;
			int k = -1;
			for (int j = 0; j < n; j++)
			{
				if (m > b[j] && b[j] > a[i] && !used[j])
				{
					m = b[j];
					k = j;
				}
			}
			if (k == -1)
			{
				for (int j = 0; j < n; j++)
				{
					if (m > b[j] && !used[j])
					{
						m = b[j];
						k = j;
					}
				}
				used[k] = 1;
				score++;
			}
			else
			{
				used[k] = 1;
			}
		}
		cout << score << endl;
	}
}