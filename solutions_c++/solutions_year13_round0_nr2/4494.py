#include <iostream>
#include <vector>
#define for0(i, n) for( int i = 0; i < (n); i++)

using namespace std;

int main ()
{
	int T;
	cin >> T;
	for0(t, T)
	{
		int N, M;
		cin >> N >> M;
		vector< vector< int > > lawn (M, vector<int> ( N, 0));
		for0(j, N)
		{
			for0(i, M)
			{
				cin >> ws >> lawn[i][j];
			}
		}
		
		vector< int > minCol (M, 0);
		vector< int > minRow (N, 0);

		for0(j, N)
		{
			int min = 1;
			for0(i, M)
			{
				if( lawn[i][j] > min) min = lawn[i][j];
			}
			minRow[j] = min;
		}
		
		for0(i, M)
		{
			int min = 1;
			for0(j, N)
			{
				if( lawn[i][j] > min) min = lawn[i][j];
			}
			minCol[i] = min;
		}


		bool possible = true;
		for0(j, N)
		{			
			for0(i, M)
			{
				if( lawn[i][j] < minRow[j] && lawn[i][j] < minCol[i] )
				{
					//cout << "i j height minCol minRow:" << i << j << lawn[i][j] << minCol[i] << minRow[j] << endl;
					 possible = false;
					 break;
				}
			}
			if( possible == false) break;
		}
		cout << "Case #" << t + 1 << ": ";
		if (possible) cout << "YES" << endl;
		else cout << "NO" << endl;
	}


}