#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	int grass[100][100];

	for (int t = 0; t < T; t++)
	{
		bool possible = true;

		int N, M;
		cin >> N >> M;

		for (int r = 0; r < N; r++)
			for (int c = 0; c < M; c++)
				cin >> grass[r][c];

		for (int r = 0; r < N; r++)
			for (int c = 0; c < M; c++)
			{
				int here = grass[r][c];

				bool a = true, b = true;
				for (int k = 0; k < N; k++)
					if (grass[k][c] > here)
						a = false;

				for (int k = 0; k < M; k++)
					if (grass[r][k] > here)
						b = false;

				if (!a && !b) possible = false;
				if (!possible) break;
			}

		cout << "Case #" << (t+1) << ": " << (possible ? "YES" : "NO") << endl;
	}

	return 0;
}