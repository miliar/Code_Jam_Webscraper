// Qualification Round 2013
// Problem A. Tic-Tac-Toe-Tomek
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int k = 0; k < T; k++)
    {
		int N, M;
		cin >> N >> M;
        vector < vector < int > > lawn(N);
		vector < vector < int > > copy(N);
		for (int i = 0; i < N; i++)
		{
			lawn[i] = vector<int>(M);
			copy[i] = vector<int>(M, 101);
			for (int j = 0; j < M; j++)
				cin >> lawn[i][j];
		}
		
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				int cur = lawn[i][j];
				bool isCuttable = true;
				for (int l = 0; l < M; l++)
					if (lawn[i][l] > cur)
					{
						isCuttable = false;
						break;
					}
				if (isCuttable)
				{
					for (int l = 0; l < M; l++)
						if (copy[i][l] >= cur)
							copy[i][l] = cur;
				}
				isCuttable = true;
				for (int l = 0; l < N; l++)
					if (lawn[l][j] > cur)
					{
						isCuttable = false;
						break;
					}
				if (isCuttable)
				{
					for (int l = 0; l < N; l++)
						if (copy[l][j] >= cur)
							copy[l][j] = cur;
				}
			}
		}

		string res = "YES";
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (copy[i][j] != lawn[i][j])
				{
					res = "NO";
					goto result;
				}
		result:
        cout << "Case #" << k+1 << ": " << res << endl;
    }
    return 0;
}