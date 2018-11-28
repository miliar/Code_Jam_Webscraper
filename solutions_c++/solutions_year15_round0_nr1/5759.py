#include <iostream>
#include <fstream>

using namespace std;


int * changeToInt( char * a , int size )
{	
	int * arr = new int [size];

	for ( int i = 0; i < size; i++ )
	{
		arr [i] = a [i] - '0';
	}
	return arr;
}


int main()
{
	fstream file ;
	
	file.open("A-large.in");

	int cases = 0;
	file >> cases;

	fstream fout;
	fout.open ("output.txt" , ios::out);

	for ( int j = 1; j <= cases+1 / 2; j++ )
	{
		int size = 0;
		file >> size;
		size++;


		char * input = new char [size];
		file >> input;

		int * arr = changeToInt( input , size );


		int standing = 0;
		int friends = 0;

		for ( int i = 0; i < size; i++ )
		{
				while ( standing < i )
				{
					friends++;
					standing += 1;
				}
				if ( standing >= i )
				{
					standing += arr [i];
				}
		}

		fout  << "Case #" << j << ": " << friends << "\n" ;
	}
	fout.close();
	file.close();
	return 0;
}