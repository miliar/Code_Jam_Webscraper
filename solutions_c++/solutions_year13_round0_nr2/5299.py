#include<iostream>
#include<fstream>
using namespace std;


bool checkColumn(int** a, int key, int i, int n)
{
	for(int j=0; j<n; j++)
	{
		if(a[i][j] > key)
			return false;
	}
	return true;
}

bool checkRow(int** a, int key, int j, int m)
{
	for(int i=0; i<m; i++)
	{
		if(a[i][j] > key)
			return false;
	}
	return true;
}

int main()
{

	ofstream fout("result.rtf");
	int T;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		int m, n;

		cin >> m >> n;

		int **a = NULL;

		a = new int *[m] ;

		for( int i = 0 ; i < m ; i++ )
		a[i] = new int[n];
		for( int i = 0 ; i < m ; i++ )
		{
			for(int j=0; j<n; j++)
			{
				cin >> a[i][j];
			}
			cin;
		}
		
		bool possible = true;




		for( int i = 0 ; i < m && possible ; i++ )
		{
			for(int j = 0; j < n && possible; j++)
			{
					if(!( checkColumn(a, a[i][j], i, n) || checkRow(a, a[i][j], j, m)))
						possible = false;
			}
		}



		if(possible)
		{
			cout << "Case #" << i+1 << ": " << "YES" << endl;
			fout << "Case #" << i+1 << ": " << "YES" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << "NO" << endl;
			fout << "Case #" << i+1 << ": " << "NO" << endl;
		}



		for( int i = 0 ; i < m ; i++ )
		delete [] a[i] ;
		delete [] a ;


	}
	system("pause");
}