#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;

#define REP( i, N) for( int i = 0; (i < N); i ++ )
#define REP2( i , limit, N ) for( int i = limit; (i < N); i++ )

typedef vector<float> vi;
typedef vi::iterator vit;

int case_number;

void main2()
{
	int row1, row2;
	cin >> row1 ;

	row1 --;

	int arr[4][4];

	REP( i , 4 )
		REP( j , 4 )
	{
		cin >> arr[i][j];
	}

	vector<int> row1_arr ;
	REP( i , 4 )
	{
		row1_arr.push_back( arr[row1][i] );
	}

	cin >> row2;
	row2--;

	REP( i , 4 )
		REP( j , 4 )
	{
		cin >> arr[i][j];
	}

	vector<int> row2_arr ;
	REP( i, 4 )
	{
		row2_arr.push_back( arr[row2][i] ); 
	}

	int common = 0;
	int value = 0;

	REP( i , 4 )
		REP ( j, 4 )
	{
		if( row1_arr[i] == row2_arr[j] )
		{
			common ++;
			value = row1_arr[i];
		}
	}

	cout << "Case #" << ++case_number << ": ";
	if( common > 1 )
	{
		cout << "Bad magician!" << endl;
		return;
	}
	if( common  == 0 )
	{
		cout << "Volunteer cheated!" << endl;
		return;
	}
	
	cout << value << endl;
}

int main()
{
	int T;
	cin >> T;
	REP( i, T )
	{
		main2();
	}

}