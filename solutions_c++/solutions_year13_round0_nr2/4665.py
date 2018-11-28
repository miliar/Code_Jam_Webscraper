#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;

	const int MAXN = 100, MAXM = 100;
	static char m[MAXN][MAXM];
	static char rowMax[MAXM];
	static char colMax[MAXN];

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int N, M;
		cin >> N >> M;

		memset(m, 0, sizeof(m));
		memset(rowMax, 0, sizeof(rowMax));
		memset(colMax, 0, sizeof(colMax));
		for (int r = 0; r < N; r++)
			for (int c = 0; c < M; c++)
			{
				int h;
				cin >> h;

				m[r][c] = h;
				rowMax[r] = max(rowMax[r], m[r][c]);
				colMax[c] = max(colMax[c], m[r][c]);
			}

		bool possible = true;
		for (int r = 0; r < N && possible; r++)
			for (int c = 0; c < M && possible; c++)
				if (m[r][c] < rowMax[r] && m[r][c] < colMax[c])
					possible = false;

		cout << "Case #" << nTestCase << ": " << (possible ? "YES" : "NO") << endl;
	}
}
