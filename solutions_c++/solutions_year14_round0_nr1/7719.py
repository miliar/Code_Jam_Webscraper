#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>


#define rep(i,n) for( int i = 0; i < n; i++ )

using namespace std;

int main()
{
	ofstream output("A-small-attempt0.out");
	ifstream input("A-small-attempt0.in");

	cin.rdbuf( input.rdbuf() );
	cout.rdbuf( output.rdbuf() );

	int T;
	cin >> T;

	rep(t,T)
	{
		int ans1, ans2;
		int mat1[4][4], mat2[4][4];

		cin >> ans1;
		rep( i, 4 )
			rep( j, 4 )
				cin >> mat1[i][j];
		cin >> ans2;
		rep( i, 4 )
			rep( j, 4 )
				cin >> mat2[i][j];

		int magicNumber = -1;
		int answers = 0;
		rep( i, 4 )
		{
			rep(j, 4 )
			{
				if( mat1[ans1-1][i] == mat2[ans2-1][j] )
				{
					magicNumber = mat1[ans1-1][i];
					answers++;
				}
			}
		}

		if( answers == 1 )
		{
			cout << "Case #" << t+1 << ": " << magicNumber << endl;
		}
		else if( answers == 0 )
		{
			cout << "Case #" << t+1 << ": Volunteer cheated!" << endl;
		}
		else 
		{
			cout << "Case #" << t+1 << ": Bad magician!" << endl;
		}
	}

	return 0;
}