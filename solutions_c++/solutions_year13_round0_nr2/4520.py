#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <deque>

using namespace std;

int main (int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t += 1)
	{
		int N,M;
		cin >> N >> M;
		vector<vector <int> > matrix (N,vector<int> (M,0));
		for (int i = 0; i < N; i += 1)
		{
			for (int j = 0; j < M; j += 1)
			{
				cin >> matrix[i][j];
			}
		}
		bool doable = true;
		for (int i = 0; i < N; i += 1)
		{
			for (int j = 0; j < M; j += 1)
			{
				int maxou = matrix[i][j];
				bool ligne = true;
				bool colonne = true;
				for (int k = 0; k < N; k += 1)
				{
					ligne = ligne && (matrix[k][j] <= maxou);
				}
				for (int k = 0; k < M; k += 1)
				{
					colonne = colonne && (matrix[i][k] <= maxou);
				}
				doable = doable && (ligne or colonne);
			}
		}
		cout << "Case #" << t+1 << ": ";
		if (doable)
		{
			cout << "YES" << endl;
		}
		else cout << "NO" << endl;
	}
	return 0;
}
