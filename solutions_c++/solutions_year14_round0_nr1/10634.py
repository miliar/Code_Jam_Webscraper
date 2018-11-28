#include<iostream>
#include<fstream>
using namespace std;

bool checkForUnique( int val , int mat[][4] , int i )
{
	for( int k = 0 ; k < i ; k++ )
	{
		for( int l = 0 ; l < 4 ; l++ )
		{
			if( val == mat[k][l] )
				return false;
		}
	}
	return true;
}

int main()
{
	int T, ans1 , ans2 , cases = 1;
	fstream fin , fout;
	fin.open( "sub-1.in" , ios::in );

	fout.open( "output.txt" , ios::out );

	fin >> T;
	if( T < 1 || T > 100 )
	{
		cout << "Not a valid no of test cases\n";
		exit(0);
	}
	while( cases <= T )
	{
		fin >> ans1;
		if( ans1 < 1 || ans1 > 4 )
		{
			cout << "Not a valid answer\n";
			exit(0);
		}

		int mat[4][4] , val , x = 0 , mat1[4][4];
		int arr[4];
		bool present = false; 
		for( int i = 0 ; i < 4 ; i++ )
		{
			for( int j = 0 ; j < 4 ; j++ )
			{
				fin >> val;
				if(!checkForUnique( val , mat , i ))
				{
					cout << "Uniqueness not found\n";

				}
				mat[i][j] = val;
				if( i == (ans1 - 1) )
				{
					arr[x] = mat[i][j];
					x++;
				}

			}
		}
		fin >> ans2;
		if( ans2 < 1 || ans2 > 4 )
		{
			cout << "Not a valid answer\n";
			exit(0);
		}

		for( int i = 0 ; i < 4 ; i++ )
		{
			for( int j = 0 ; j < 4 ; j++ )
			{
				fin >> val;
				if(!checkForUnique( val , mat1 , i ))
				{
					cout << "Uniqueness not found\n";

				}
				mat1[i][j] = val;
			}
		}

		int count = 0 , p = 0 , index;
		for( int e = 0 ; e < 4 ; e++ )
		{
				p = 0;
				for( ; p < 4 ; p++ )
				{
					if( mat1[ans2-1][e] == arr[p] )
					{
						count++;
						if( count == 1 )
							index = p;
					}
					
				}
		}
		if( count > 1 )
			cout << "Case #"<<cases<<": Bad magician!"<<endl;
		else if( count == 1 )
			cout << "Case #" << cases <<": " <<  arr[index] << endl;
		else
			cout << "Case #" << cases << ": Volunteer cheated!" << endl;

		cases++;
	}
	fin.close();
	fout.close();
	return 0;
}