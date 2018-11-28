#include<iostream>
#include<fstream>

using namespace std;

int main ()
{
	ifstream fin ( "A-small-attempt0.in" );
	ofstream fout ( "output.txt" );
	if ( !fin )
	{
		cout << "Error! file not found." << endl;
		exit(0);
	}
	int cases;
	fin >> cases;

	if ( cases < 1 || cases > 100 )
	{
		fout << "Invalid No. of cases." << endl;
	}
	for ( int i = 0 ; i < cases ; i++ )
	{
		int arr1[4][4];
		int arr2[4][4];
		int arr[2][4];
		
		int ans1 , ans2;

		fin >> ans1;
		if ( ans1 < 1 || ans1 > 4 )
		{
			fout << "First Answer is incorrect." << endl;
			break;
		}
		for ( int j = 0 ; j < 4 ; j++ )
		{
			for ( int k = 0 ; k < 4 ; k++ )
			{
				fin >> arr1[j][k];
			}
		}

		fin >> ans2;
		if ( ans2 < 1 || ans2 > 4 )
		{
			fout << "Second Answer is incorrect." << endl;
			break;
		}
		int a;
		for ( int j = 0 ; j < 4 ; j++ )
		{
			for ( int k = 0 ; k < 4 ; k++ )
			{
				fin >>arr2[j][k];
			}
		}
	
		for ( int j = 0 ; j < 4 ; j++ )
		{
			if ( j+1 == ans1 )
			{
				for ( int k = 0 ; k < 4 ; k++ )
				{
					arr[0][k] = arr1[j][k];
				}
			}
		}

		for ( int j = 0 ; j < 4 ; j++ )
		{
			if ( j+1 == ans2 )
			{
				for ( int k = 0 ; k < 4 ; k++ )
				{
					arr[1][k] = arr2[j][k];
				}
			}
		}

		

		int c[4] = {0};
		for ( int j = 0 ; j < 4 ; j++ )
		{
			for ( int k = 0 ; k < 4 ; k++ )
			{
				if ( arr[0][j] == arr[1][k] )
				{
					c[j]++;
				}
			}
			
		}

		if ( c[0] == 0 && c[1] == 0 && c[2] == 0 && c[3] == 0 )
		{
			fout << "Case #"<<i + 1 << ": " << "Volunteer cheated!" << endl;
		}
		else if ( c[0] + c[1] + c[2] + c[3] > 1 )
		{
			fout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
		}
		else if ( c[0] + c[1] + c[2] + c[3] == 1 )
		{
			fout << "Case #" << i+1 << ": ";
			
			for ( int j = 0 ; j < 4 ; j++ )
			{
				for ( int k = 0 ; k < 4 ; k++ )
				{
					if ( arr[0][j] == arr[1][k] )
					{
						fout << arr[0][j] << endl;
					}
				}
			
			}
		}
	}
	fout .close();
	fin.close();
	return 0;
}