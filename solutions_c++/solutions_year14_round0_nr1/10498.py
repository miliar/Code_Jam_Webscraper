// GoogleCodeJam2014A.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 3 )
		return 0;

	_TCHAR* fileName = argv[ 1 ];

	ifstream ifs( fileName );
	if( ifs.is_open() == false )
		return 0;

	fileName = argv[ 2 ];
	ofstream ofs( fileName, ios::out );
	if( ofs.is_open() == false )
		return 0;

	int n;
	ifs >> n;

	int line1, line2;
	int cards1[ 4 ][ 4 ];
	int cards2[ 4 ][ 4 ];
	for( int i = 0; i < n; i++ )
	{
		ifs >> line1;
		for( int r = 0; r < 4; r++ )
			for( int c = 0; c < 4; c++ )
				ifs >> cards1[ r ][ c ];

		ifs >> line2;
		for( int r = 0; r < 4; r++ )
			for( int c = 0; c < 4; c++ )
				ifs >> cards2[ r ][ c ];

		int card = -1;
		int found = 0;
		for( int c1 = 0; c1 < 4; c1++ )
		{
			for( int c2 = 0; c2 < 4; c2++ )
			{
				if( cards1[ line1 - 1 ][ c1 ] == cards2[ line2 - 1 ][ c2 ] )
				{
					card = cards1[ line1 - 1 ][ c1 ];
					found++;
					break;
				}
			}
		}

		ofs << "Case #" << i+1 << ": ";
		switch( found )
		{
		case 0:
			ofs << "Volunteer cheated!" << endl;
			break;
		case 1:
			ofs << card << endl;
			break;
		default:
			ofs << "Bad magician!" << endl;
			break;
		}
	}

	ifs.close();
	ofs.close();

	return 0;
}

