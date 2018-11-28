#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool check_if_possible( vector< vector< int >>, int, int, int, int );

int main()
{
	ifstream infl( "B-large.in" );
	ofstream outfl( "lawnmower_large.txt" );
	
	int num_of_tests;
	int N_metre;
	int M_metre;
	int input;

	int case_num = 0;
	
	infl >> num_of_tests;

	while( case_num < num_of_tests )
	{
		infl >> N_metre;
		infl >> M_metre;

		bool is_possible;

		vector< vector< int >> lawn ( N_metre, vector< int >( M_metre ));

		for( int row = 0; row < N_metre; row++ )
		{
			for( int col = 0; col < M_metre; col++ )
			{
				infl >> input;
				lawn[ row ][ col ] = input;
			}
		}

		case_num++;

		for( int row = 0; row < N_metre; row++ )
		{
			for( int col = 0; col < M_metre; col++ )
			{
				is_possible = check_if_possible( lawn, M_metre, N_metre, row, col );
				if( !is_possible )
				{ 
					outfl << "Case #" << case_num << ": NO" << endl; 
					goto end_loop;
				}
			}
		}

end_loop:

		if( is_possible )
		{ outfl << "Case #" << case_num << ": YES" << endl;  }
		
		//for( int row = 0; row < N_metre; row++ )
		//{
		//	for( int col = 0; col < M_metre; col++ )
		//	{  cout <<  lawn[ i ][ j ];  }
	
		//	cout << endl;
		//}

		//cout << endl;



		//infl >> N_metre;
		//infl >> M_metre;
		//vector< vector< int >> lawn ( N_metre, vector< int >( M_metre ) );

		//int N_counter = 0;

		//while( N_counter < N_metre )
		//{
		//	int M_counter = 0;

		//	while( M_counter < M_metre )
		//	{
		//		infl >> input;
		//		lawn[ N_counter ][ M_counter ] = input;
		//		M_counter++; 
		//	}

		//	N_counter++;
		//}

		//case_num++;

		//N_counter = 0;

		//while( N_counter < N_metre )
		//{
		//	int M_counter = 0;

		//	while( M_counter < M_metre )
		//	{
		//		cout << lawn[ N_counter ][ M_counter ];
		//		M_counter++;
		//	}

		//	cout << endl;

		//	N_counter++;
		//}

	}
}

bool check_if_possible( vector< vector< int >> lawn, int M_metre, int N_metre, int row, int col )
{
	int num = lawn[ row ][ col ];

	// Check row
	for( int i = 0; i < M_metre; i++ )
	{
		if( lawn[ row ][ i ] > num )
		{
			// Check column
			for( int j = 0; j < N_metre; j++ )
			{
				if( lawn[ j ][ col ] > num )
				{  return false;  }
			}

			return true;
		}
	}

	return true;
}