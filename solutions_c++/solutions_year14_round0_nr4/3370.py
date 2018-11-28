#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;

	for ( int test = 1 ; test <= T ; ++test )
	{
		int n;

		cin >> n;

		vector<double> a(n);
		vector<double> b(n);

		for ( int i = 0 ; i < n ; ++i )
			cin >> a[i];

		for ( int i = 0 ; i < n ; ++i )
			cin >> b[i];

		std::sort(a.begin(), a.end());
		std::sort(b.begin(), b.end());

		int curr = 0;
		int solveWar = 0;

		for ( int i = 0 ; i < n ; ++i )
		{
			while ( curr < n )
			{
				if ( a[i] > b[curr] )
				{
					curr++;
					solveWar++;
				}
				else break;
			}
			curr++;
		}

		int solveWarDeceitful = 0;
		int l = 0;
		int r = n-1;
		for ( int i = 0 ; i < n ; ++i )
		{
			if ( a[i] > b[l] )
			{
				solveWarDeceitful++;
				l++;
			}
			else {
					r--;
				 }
		}

		std::cout << "Case #" << test << ": " << solveWarDeceitful << " " << solveWar << std::endl;
	}
}


/*#include <iostream>
#include <iomanip>

char a[100][100];

int main()
{
	int T = 0;
	std::cin >> T;

	for ( int test = 1 ; test <= T ; ++test )
	{
		int n,m,k;
		std::cin >> n >> m >> k;

		for ( int i = 0 ; i <= n ; ++ i )
		{
			for ( int j = 0 ; j <= m ; ++j )
			{
				a[i][j] = '.';
			}
		}

		std::cout << "Case #" << test << ":" << std::endl;

		if (( m == 1 ) || ( n == 1 ))
		{
			if ( k > m*n-2)
			{
				std::cout << "Impossible" << std::endl;
				continue;
			}
		}
		else  if ( k > m*n-4 )
		{
			std::cout << "Impossible" << std::endl;
			continue;
		}

		for ( int p = 1 ; p <= n+m ; ++p )
		{
			for ( int i = 1 ; i <= n ; ++i )
				for ( int j = 1 ; j <= m ; ++j )
					if ( i+j == p )
					{
						if (!(( j > m-2 ) && ( i > n-2 )))
						{
	  						if ( k > 0 )
							{					
								a[i][j] = '*';
								--k;
							}
						}
					}
		}

		a[n][m] = 'c';

		for ( int i = 1 ; i <= n ; ++i )
		{
			for ( int j = 1 ; j <= m ; ++j )
			{
				std::cout << a[i][j];
			}
			std::cout << std::endl;
		}
	}
}
*/