#include <iostream>
#include <string>
#include <cstdlib>
#include <map>
#include <vector>

using namespace std;

int main()
{
	unsigned T;
	cin >> T;

	for (unsigned i = 0; i < T; i++)
	{
		int N, M;
		cin >> N >> M;

		cout << "Case #" << i + 1 << ": ";

		bool can_cut = true;
		int lawn[N][M];

		// Grab each row
		for (unsigned j = 0; j < N; j++)
		{
			// Grab each cell
			for (unsigned k = 0; k < M; k++)
			{
				cin >> lawn[j][k];
			}
		}

		if (N == 1 || M == 1)
		{
			cout << "YES" << endl;
			continue;
		}

		map<int, int> row;
		map<int, int> col;
		
		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				if (row[j] < lawn[j][k]) row[j] = lawn[j][k];
				if (col[k] < lawn[j][k]) col[k] = lawn[j][k];
			}
		}
		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				if (lawn[j][k] < row[j] && lawn[j][k] < col[k])
					can_cut = false;
				if (!can_cut) break;
			}
			if (!can_cut) break;
		}


		cout << ((can_cut) ? "YES" : "NO") << endl;
	}

	return 0;
}
