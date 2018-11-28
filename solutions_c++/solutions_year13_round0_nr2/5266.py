#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	int counter = 0;
	
	while( T-- )
	{
		counter++;
		
		int N,M;
		cin >> N >> M;
		
		int table[N][M];
		int maxof[N];
		int maxam[M];
		
		for (int i = 0; i < N; i++)
		{
			maxof[i] = -1;
		}
		
		for (int i = 0; i < M; i++)
		{
			maxam[i] = -1;
		}
		
				
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				cin >> table[i][j];
				if( table[i][j] > maxof[i]  )
				{
					maxof[i] = table[i][j];
				}
			}
		}

		for (int i = 0; i < M; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if( table[j][i] > maxam[i]  )
				{
					maxam[i] = table[j][i];
				}
			}
		}
		
		int mark = 0;
		
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if( table[i][j] >= maxof[i] || table[i][j] >= maxam[j] )
				{
					mark++;
				}
			}	
		}
		
		cout << "Case #" << counter << ": ";
		if( mark == N*M )
		{
			cout << "YES" << endl;
		}
		else
		{
			cout << "NO" << endl;
		}
	}
	
	return 0;
}
