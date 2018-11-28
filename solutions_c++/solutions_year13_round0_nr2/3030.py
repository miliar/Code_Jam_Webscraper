#include <iostream>
#include <fstream>

using namespace std;

int n , m ;
int A[100][100];

int valid ( int r , int c ) {

	int flg = 1;
	int i ;

	for ( i = 0 ; i < m ; i++ ) 
		if ( A[r][i] > A[r][c] ) flg = 0;

	if ( flg == 1 ) return flg ;

	flg = 1;

	for ( i = 0 ; i < n ; i++ ) 
		if ( A[i][c] > A[r][c] ) flg = 0;

	return flg;
}

int Pos (){

	int flg = 1;
	int i , j ;

	for ( i = 0 ; i < n ; i++ ) 
		for ( j = 0 ; j < m ; j++ ) {
			int val = valid ( i , j ) ;
			if ( val == 0 ) flg = 0;
	}

	return flg;
}

void Readata(){

	ifstream fin("B.in");
	
	int T;
	fin >> T;

	int i;
	for ( i = 1 ; i <= T ; i++ ) {

		fin >> n >> m;

		int j , k ;

		for ( j = 0 ; j < n ; j++ ) 
			for ( k = 0 ; k < m ; k++ ) 
				fin >> A[j][k];

		int flg = Pos();

		if ( flg == 1 ) cout << "Case #" << i << ": YES" << endl;
		if ( flg == 0 ) cout << "Case #" << i << ": NO" << endl;
		
	}
}

int main()
{
	Readata();
	return 0;
}
