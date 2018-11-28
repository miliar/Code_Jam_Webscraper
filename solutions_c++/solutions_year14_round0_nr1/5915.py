#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

ifstream in;
ofstream out;

void loadTable( int *table )
{
	for ( int i = 0; i < 16; ++i )
	{
		in >> table[ i ];
	}
};

vector< int > intersect( int *a, int *b )
{
	vector< int > intersectionSet;

	for ( int x = 0; x < 4; ++x )
	{
		for ( int y = 0; y < 4; ++y )
		{
			if ( a[ x ] == b[ y ] )
			{
				intersectionSet.push_back( a[ x ] );
				break;
			}
		}
	}
	
	return intersectionSet;
};

int main( int argc, char **argv )
{
	in.open( "A_in.txt" );
	out.open( "A_out.txt" );
	
	if ( !in.is_open() )
	{
		cout << "Error: input file not found!" << endl;
		return -1;
	}
	
	if ( !out.is_open() )
	{
		cout << "Error: output file could not be opened!" << endl;
		in.close();
		return -1;
	}
	
	int nTests;
	in >> nTests;
	
	
	for ( int i = 0; i < nTests; ++i )
	{
		int ans1, ans2;
		int arr1[4][4], arr2[4][4];
		
		in >> ans1;
		loadTable( arr1[ 0 ] );
		in >> ans2;
		loadTable( arr2[ 0 ] );
		
		ans1--; ans2--; // get indices from 0 to 3
		
		vector< int > possibilities = intersect( arr1[ ans1 ], arr2[ ans2 ] );
		
		if ( possibilities.size() == 0 )
		{
			out << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		}
		else if ( possibilities.size() == 1 )
		{
			out << "Case #" << i + 1 << ": " << possibilities[ 0 ] << endl;
		}
		else
		{
			out << "Case #" << i + 1 << ": Bad magician!" << endl;
		}
	}
	
	in.close();
	out.close();
	return 0;
};