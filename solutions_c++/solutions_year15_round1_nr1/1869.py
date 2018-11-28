#include <iostream>

using namespace std;

void solve(int *m, const int& N, int& y, int&z)
{
	
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		int N;
		cin >> N;
		int *m = new int[N];

		int y = 0;
		int maxv = 0;
		for (int j = 0; j < N; j++)
		{
			cin >> m[j];
			if (j > 0)
			{
				if (m[j] < m[j - 1])
				{
					int t = m[j - 1] - m[j];
					y += t;
					maxv = maxv > t ? maxv : t;
				}
			}
		}

		int z = 0;
		for (int j = 0; j < N - 1; j++)
		{
			if (m[j] < maxv)
			{
				z += m[j];
			}
			else
			{
				z += maxv;
			}
		}

		cout << "Case #" << i << ": " << y << " " << z << endl;

		delete[] m;
	}

	return 0;
}