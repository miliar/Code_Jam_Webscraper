// gcjqB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

const int MAX_MATRIX_SIZE = 256;

using namespace std;

template <typename T>
T StringToNumber ( string &Text )
{
	istringstream ss(Text);
	T result;
	return ss >> result ? result : 0;
}

void getLineNumbers( string& strLine , vector<int>& numbers ) 
{
	const char* str = strLine.c_str();
	
	int pos = -1;
	int numPos = 0;
	while( ++pos < strLine.size() ) {
		if( ( str[pos] < '0' ) || ( str[pos] > '9' ) ) {
			continue;
		}

		numbers[numPos++] = atoi( &str[pos] );

		while( ( pos < strLine.size() ) && ( str[pos] >= '0' ) && ( str[pos] <= '9' ) ) {
			pos++;
		}
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	if( argc > 3 || argc == 1 ) {
		cout << "invalid args" << endl;
		return -1;
	}

	ifstream ifs( argv[1] );
	ofstream ofs( "out.txt" );

	vector<vector<int>> matrix(MAX_MATRIX_SIZE);
	for( vector<vector<int>>::iterator it = matrix.begin() ; it != matrix.end() ; ++it ) { 
		it->resize(MAX_MATRIX_SIZE); 
	}
	
	bool finishFlags[MAX_MATRIX_SIZE][MAX_MATRIX_SIZE];

	string buf;
	vector<int> lineNumbers(MAX_MATRIX_SIZE);
	vector<int> matSize(MAX_MATRIX_SIZE);
	int nLineCount = 0;
	int nTestCount = 0;
	int nMaxTest = 0;
	while(ifs) {
		buf.clear();
		if( !getline(ifs, buf) ) {
			break;
		}
		++nLineCount;

		if( 1 == nLineCount ) {
			nMaxTest = StringToNumber<int>(buf);
			continue;
		}

		memset( finishFlags , false , sizeof( bool ) * MAX_MATRIX_SIZE * MAX_MATRIX_SIZE );
		
		cout << "[" << nTestCount << "] " << buf << endl;

		getLineNumbers( buf , matSize );
		bool bFailed = false;
		for( int i = 0 ; i < matSize[0] ; i++ ) {
			if( !getline(ifs, buf) ) {
				bFailed = true;
				break;
			}

			cout << "[" << nTestCount << "] " << buf << endl;

			getLineNumbers( buf , matrix[i] );
		}
		if( bFailed ) {
			cout << "failed to get line" << endl;
			break;
		}

		bool bPassTotal = true;
		int width = matSize[0];
		int height = matSize[1];
		for( int low = 0 ; low < width ; low++ ) {
			if( !bPassTotal ) {
				break;
			}
			for( int col = 0 ; col < height ; col++ ) {
				if( !bPassTotal ) {
					break;
				}
				if( false == finishFlags[low][col] ) {

					bool bPassSingle = true;

					finishFlags[low][col] = true;
					int num = matrix[low][col];
					// test low
					for( int i = 0 ; i < width ; i++ ) {
						if( num < matrix[i][col] ) {
							bPassSingle = false;
							break;
						}
					}
					if( bPassSingle ) {
						// set finish flag
						for( int i = 0 ; i < width ; i++ ) {
							if( num == matrix[i][col] ) {
								finishFlags[i][col] = true;
							}
						}
						continue;
					}
					// test col
					bPassSingle = true;
					for( int j = 0 ; j < height ; j++ ) {
						if( num < matrix[low][j] ) {
							bPassSingle = false;
							break;							
						}
					}
					if( bPassSingle ) {
						// set finish flag
						for( int j = 0 ; j < height ; j++ ) {
							if( num == matrix[low][j] ) {
								finishFlags[low][j] = true;
							}
						}
						continue;
					}
					else {
						cout << "Failed at (" << low << "," << col << ")" << endl;
						bPassTotal = false;
					}
				}
			}
		}

		++nTestCount;

		if( bPassTotal ) {
			cout << "Case #" << nTestCount << ": YES" << endl;
			ofs << "Case #" << nTestCount << ": YES" << endl;
		}
		else {
			cout << "Case #" << nTestCount << ": NO" << endl;			
			ofs << "Case #" << nTestCount << ": NO" << endl;			
		}


	}

	ifs.close();
	ofs.close();

	char in;
	cin.get(in);

	return 0;
}

