#include <iostream>
using namespace std;

int trawnik[101][101];
int max_in_row[101];
int max_in_col[101];

int main()
{
	ios_base::sync_with_stdio(0);
	int ilosc;
	cin >> ilosc;
	bool daSie = true;
	
	for( int zestaw = 0; zestaw < ilosc; zestaw++ )
	{
		int N, M;
		daSie = true;
		
		cin >> N;
		cin >> M;
		
		int temp;
		
		for( int i = 0; i < N; i++ )
			max_in_row[i] = 0;
			
		for( int i = 0; i < M; i++ )
			max_in_col[i] = 0;
		
		for( int n = 0; n < N; n++ )
		{
			for( int m = 0; m < M; m++ )
			{
				cin >> temp;
				
				if( temp > max_in_row[n] )
					max_in_row[n] = temp;
					
				if( temp > max_in_col[m] )
					max_in_col[m] = temp;
					
				trawnik[m][n] = temp;
			}
		}
				
		for( int n = 0; n < N; n++ )
		{
			for( int m = 0; m < M; m++ )
			{
				if( trawnik[m][n] < max_in_row[n] && trawnik[m][n] < max_in_col[m] )
				{
					daSie = false;
					break;
				}
			}
		}
		
		if( daSie )
			cout << "Case #" << (zestaw+1) << ": YES\n";
		else
			cout << "Case #" << (zestaw+1) << ": NO\n";
	}
	return 0;
}
