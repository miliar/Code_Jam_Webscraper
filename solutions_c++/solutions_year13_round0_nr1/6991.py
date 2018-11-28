#include <iostream>
#include <fstream>
using namespace std;

char mat[4][4];

int scanLine(int i, int j, int ic, int jc) {
	int x = 0, o = 0;
	for( int k = 0; k < 4; k++ ) {
		switch( mat[i][j] ) {
			case '.': return 3;
			case 'X': x++; break;
			case 'O': o++; break;
			case 'T': x++; o++; break;
		}
		i += ic;
		j += jc;
	}
	if( x == 4 )
		return 0;
	else if( o == 4 )
		return 1;
	return 2;
}

int main() {
	ifstream in;
	ofstream out;
	in.open( "A-large.in" );
	out.open( "A-large.out" );
	int count;
	in >> count;
	const int n = 4;
	const char rez[4][23] = {"X won", "O won", "Draw", "Game has not completed"};
	for( int k = 0; k < count; k++ ) {
		for( int i = 0; i < n; i++ )
			for( int j = 0; j < n; j++ )
				in >> mat[i][j];

		int iRez = 3, iLine, s = 0, p;

		for( p = 0; p < 4; p++ ) {
			iLine = scanLine(p, 0, 0, 1);
			if( iLine < 2 ) {
				iRez = iLine;
				break;
			} else if( iLine == 2 )
				s++;
		}
		if( p == 4 && s == 4 )
			iRez = 2;

		for( p = 0; p < 4; p++ ) {
			iLine = scanLine(0, p, 1, 0);
			if( iLine < 2 ) {
				iRez = iLine;
				break;
			}
		}

		iLine = scanLine(0, 0, 1, 1);
		if( iLine < 2 )
			iRez = iLine;

		iLine = scanLine(3, 0, -1, 1);
		if( iLine < 2 )
			iRez = iLine;

		out << "Case #" << ( k + 1 ) << ": " << rez[iRez] << endl;
	}
	in.close();
	out.close();
	return 0;
}