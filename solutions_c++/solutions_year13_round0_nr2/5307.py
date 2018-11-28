// O(N*M*(N+M)), but could be better, because once a row/column is checked then all the vaules in it are ok
#include <iostream>
using namespace std;

const int MAX = 100;

bool check(int lawn[MAX][MAX], int n, int m, int N, int M)
{
	bool possible = true;
	for(int i = 0; i < N && possible; i++)
		if(lawn[i][m] > lawn[n][m])
			possible = false;
	if(possible) return true;
	
	possible = true;
	for(int j = 0; j < M && possible; j++)
		if(lawn[n][j] > lawn[n][m])
			possible = false;
	if(possible) return true;

	return false;
}

int main()
{
	int T, N, M;
	bool possible;
	int lawn[MAX][MAX];
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cin >> N >> M;
		for(int n = 0; n < N; n++)
			for(int m = 0; m < M; m++)
				cin >> lawn[n][m];
		//
		possible = true;
		for(int n = 0; n < N && possible; n++)
			for(int m = 0; m < M && possible; m++)
				if(!check(lawn, n, m, N, M))
					possible = false;
		//
		cout << "Case #" << t << ": " << (possible ? "YES" : "NO") << "\n";
	}
	cout << flush;
	return 0;
}