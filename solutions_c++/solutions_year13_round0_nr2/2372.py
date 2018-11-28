#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solver
{	
public:
	string Solve()
	{
		int N, M;
		vector<vector<int>> lawn;
		vector<int> maxcol, maxrow;
		cin >> N >> M;
		lawn.resize(N);
		maxcol.resize(M, 0);
		maxrow.resize(N);
		for ( int i = 0; i < N; ++i ) {
			lawn[i].resize(M);
			for ( int j = 0; j < M; ++j ) {
				cin >> lawn[i][j];
				if ( lawn[i][j] > maxcol[j] )
					maxcol[j] = lawn[i][j];
			}
			maxrow[i] = *max_element(lawn[i].begin(), lawn[i].end());
		}
		for ( int i = 0; i < N; ++i ) {
			for ( int j = 0; j < M; ++j ) {
				if ( lawn[i][j] < maxrow[i] && lawn[i][j] < maxcol[j] )
					return "NO";
			}
		}
		return "YES";
	}
};

int main()
{
	int T;
	cin >> T;
	for ( int t = 0; t < T; ++t )
	{
		cout << "Case #" << (t+1) << ": " << Solver().Solve() << endl;
	}
	return 0;
}
