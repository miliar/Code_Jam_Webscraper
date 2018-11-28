#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

ifstream fin;
ofstream fout;

int main()
{
	fin.open("A_small.in");
	fout.open("a_small.out");
	
	int T = 0 , choose1 = 0 , choose2 = 0;
	int i , j , k , input , output;
	int candidate[8]; //because there's only 4 elements in a row
	int check; //0: no same element in the candidate[], 1: there's only 2 elements in the candidate[] are the same, 2: more than one pairs elements are the same
	
	fin >> T;
	
	for( int t = 1 ; t <= T ; ++t )
	{
		k = 0;
		fin >> choose1;
		for( i = 0 ; i < 4 ; ++i )
		{
			for( j = 0 ; j < 4 ; ++j )
			{
				fin >> input;
				if( i == choose1-1 )
				{
					candidate[ k++ ] = input;
				}
			}
		}
		
		fin >> choose2;
		for( i = 0 ; i < 4 ; ++i )
		{
			for( j = 0 ; j < 4 ; ++j )
			{
				fin >> input;
				if( i == choose2-1 )
				{
					candidate[ k++ ] = input;
				}
			}
		}
		
		sort( candidate , candidate+8 );

		//count ans
		check = 0;
		for( i = 1 ; i < k ; ++i )
		{
			if( candidate[i] == candidate[i-1] )
			{
				++check;
				output = candidate[i];
			}
		}
		
		if( check == 1 )
			fout << "Case #" << t << ": " << output << endl;
		else if( check > 1 )
			fout << "Case #" << t << ": Bad magician!" << endl;
		else //check = 0 
			fout << "Case #" << t << ": Volunteer cheated!" << endl;
	}
	
	return 0;
}
