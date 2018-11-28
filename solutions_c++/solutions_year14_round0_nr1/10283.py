# include <fstream>
# include <cstring>
# include <algorithm>

using namespace std;

ifstream f("codejam.in");
ofstream g("codejam.out");

int a[ 100 ];
int t, r, caz;

void solve()
{
	int i, doi = 0, unu = 0, indice;
	for ( i = 1 ; i <= 16 ; i++ )
	{
		if ( a[ i ] == 2 )
			doi++, indice = i;
		if ( a[ i ] == 1 )
			unu++;
	}
	
	if ( doi == 1 )
		g << "Case #" << caz << ": " << indice << "\n";
	else
	if ( doi > 1 )
		g << "Case #" << caz << ": Bad magician!" << "\n";
	else
		g << "Case #" << caz << ": Volunteer cheated!" << "\n";
}

void reset()
{
	int i;
	for ( i = 1 ; i <= 16 ; i++ )
		a[ i ] = 0;
}

int main()
{
	int k, i, j, x, nr;
	f >> t;
	for ( k = 1 ; k <= t ; k++ )
	{
		caz = k;
		nr = 2;
		while ( nr )
		{
			f >> r;
			for ( i = 1 ; i <= 4 ; i++ )
				for ( j = 1 ; j <= 4 ; j++ )
				{
					f >> x;
					if ( i == r )
						a[ x ]++;
				}
		  nr--;
		}
		solve();
		reset();
	}
	return 0;
}