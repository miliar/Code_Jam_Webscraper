
#include "stdafx.h"

#include <stdlib.h>
#include <math.h>

#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iomanip>

using namespace std;

const string OUTPUT_FILENAME = "output.txt";

template <typename T>
T StringToNumber ( const string &Text )
{
	istringstream ss(Text);
	T result;
	return ss >> result ? result : 0;
}

vector<string> &split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

struct TestData {
	long R;
	long C;
	long M;
};

struct InputDataSet {
	int T;
	vector<TestData> vecData;
};

void Calc( InputDataSet& data , ofstream& ofs ) 
{
	long long output = 0;

	//cout << "Input (" << data.lineNumber << ") " << data.name << " n=" << data.n << endl;

	for( int i = 0; i < data.vecData.size() ; i++ ) {
		TestData test = data.vecData.at(i);
		char ans[52][52] = {};
		//memset( ans , 0 , test.R*test.C );

		cout << i << " M:" << test.M << " R:" << test.R << " C:" << test.C << endl;

		bool bFailed = false;
		int nFreeSpaceCount = test.C * test.R - test.M;
		int nRestFreeSpaceCount = nFreeSpaceCount;

		if( i == 178 ) {
			bFailed = false;
		}

		do {
			if( test.M == 0 ) {
				// ���e���O�̏ꍇ�͖������Ő���
				for( int j = 0 ; j < test.R ; j++ ) {
					for( int k = 0 ; k < test.C ; k++ ){
						if( ans[j][k] == 0 ) {
							ans[j][k] = '.';
						}
					}
				}
				break;
			}
			if( nRestFreeSpaceCount == 1 ) {
				// �c�肪�P�̏ꍇ�͂ǂ�Ȍ`��ł�����
				break;
			}
			if( test.C == 1 || test.R == 1 ) {
				// 1 �s���P��̍s��
				// ��ɃZ�[�t
				for( int j = 0 ; j < test.R ; j++ ) {
					for( int k = 0 ; k < test.C ; k++ ) {
						if( 0 == ans[j][k] ) {
							ans[j][k] = '.';
							nRestFreeSpaceCount--;
						}
						if( nRestFreeSpaceCount <= 0 ) {
							break;
						}
					}
					if( nRestFreeSpaceCount <= 0 ) {
						break;
					}
				}
			}
			if( test.C == 2 || test.R == 2 ) {
				// 2�Ɗ�͑S��
				if( ( nFreeSpaceCount == 2 ) ||
					( nFreeSpaceCount % 2 == 1 ) ) {
					bFailed = true;
					break;
				}

				if( test.C == 2 ) {
					for( int j = 0 ; j < test.R ; j++ ) {
						ans[j][0] = '.';
						ans[j][1] = '.';
						nRestFreeSpaceCount-=2;
						if( nRestFreeSpaceCount <= 0 ) {
							break;
						}
					}
					if( nRestFreeSpaceCount <= 0 ) {
						break;
					}
				}
				else {
					for( int j = 0 ; j < test.C ; j++ ) {
						ans[0][j] = '.';
						ans[1][j] = '.';
						nRestFreeSpaceCount-=2;
						if( nRestFreeSpaceCount <= 0 ) {
							break;
						}
					}
					if( nRestFreeSpaceCount <= 0 ) {
						break;
					}
				}
			}
			if( test.C >= 3 && test.R >= 3 ) {
				// �s������R�ȏ�
				bool bBreak = false;
				switch( nFreeSpaceCount ) {
				case 1: //  �����ɂ͓���Ȃ�
				case 2:
				case 3:
				case 5:
				case 7:
					bFailed = true;
					break;
				case 4:
					ans[0][0]= '.';
					ans[0][1]= '.';
					ans[1][0]= '.';
					ans[1][1]= '.';
					bBreak = true;
					break;
				case 6:
					ans[0][0]= '.';
					ans[0][1]= '.';
					ans[0][2]= '.';
					ans[1][0]= '.';
					ans[1][1]= '.';
					ans[1][2]= '.';
					bBreak = true;
					break;
				default:
					// 8 �ȏ�
					break;
				}
				if( bFailed || bBreak ) {
					break;
				}

				// 8�ȏ�̏ꍇ
				// �Œ蕔��
				ans[0][0]= '.';
				ans[0][1]= '.';
				ans[0][2]= '.';
				ans[1][0]= '.';
				ans[1][1]= '.';
				ans[1][2]= '.';
				ans[2][0]= '.';
				ans[2][1]= '.';

				nRestFreeSpaceCount -= 8;

				int RRow = 0;
				int RCol = 3;
				int BRow = 3;
				int BCol = 0;

				int lastPosR = 2;
				int lastPosC = 2;
				
				bool bTestRight = true;

				while(1) {
					if( nRestFreeSpaceCount == 1 ) {
						ans[lastPosR][lastPosC] = '.';
						break;
					}
					if( nRestFreeSpaceCount == 0 ) {
						break;
					}

					if( bTestRight ) {
						// ���ɖ��߂Ă����^�[��
						if( ( RCol < test.C ) && 
							( RRow + 1 < test.R ) ) {
							ans[RRow][RCol]= '.';
							ans[RRow+1][RCol]= '.';
							if( RRow == lastPosR ) {
								// ��p�̒u���ꏊ���㏑�������ꍇ
								if( lastPosR + 2 >= test.R ) {
									lastPosC += 1;
								}
								else {
									lastPosR += 2;
								}
							}
							RCol++;
							nRestFreeSpaceCount -= 2;
						}
						else {
							// ���ɖ��߂�^�[���ɕύX
							bTestRight = false;
							RCol = BCol + 2; // ����J�n�ʒu
							RRow += 2;
							if( RRow + 1 >= test.R )  {
								// ���ɖ߂�
								RRow -= 2;
								// ����ȏと�͎��{���Ȃ�
								RCol = test.C;
							}
						}
					}
					else {
						// ���ɖ��߂Ă����^�[��
						if( ( BRow < test.R ) && 
							( BCol + 1 < test.C )) {
							ans[BRow][BCol]= '.';
							ans[BRow][BCol+1]= '.';
							nRestFreeSpaceCount -= 2;
							if( BCol == lastPosC ) {
								// ��p�̒u���ꏊ���㏑�������ꍇ
								if( lastPosC + 2 >= test.C ) {
									lastPosR += 1;
								}
								else {
									lastPosC += 2;
								}
							}
							BRow++;
						}
						else {
							// ���ɖ��߂�^�[���ɕύX
							bTestRight = true;
							BRow = RRow + 2; // ����J�n�ʒu
							BCol += 2;
							if( BCol + 1 >= test.C )  {
								// ���ɖ߂�
								BCol -= 2;
								// ����ȏ㉺�͎��{���Ȃ�
								BRow =  test.R;
							}
						}
					}
				}
			}
		}while(0);
		// �c����}�C���Ŗ��߂�
		for( int j = 0 ; j < test.R ; j++ ) {
			for( int k = 0 ; k < test.C ; k++ ){
				if( ans[j][k] == 0 ) {
					ans[j][k] = '*';
				}
			}
		}
		// 00 �Ƀ`�F�b�N������
		ans[0][0] = 'c';

		cout << "Case #" << i+1 << ":" << endl;
		ofs << "Case #" << i+1 << ":" << endl;

		if( bFailed ) {
			cout << "Impossible" << endl;
			ofs << "Impossible" << endl;
		}
		else {
			for( int j = 0 ; j < test.R ; j++ ) {
				cout << ans[j] << endl;
				ofs << ans[j] << endl;
			}
		}

		int nMines = 0;
		for( int j = 0 ; j < test.R ; j++ ) {
			for( int k = 0 ; k < test.C ; k++ ){
				if( ans[j][k] == '*' ) {
					nMines++;
				}
			}
		}
		if( !bFailed && (nMines != test.M) ) {
			cout << "invalid mines counts" << endl;
		}

		//ofs << fixed << setprecision(7) 
		//	<< "Case #" << i+1 << ": " 
		//	<< timeTotalPrev << endl;

		// test bad magician
		//cout << "Case #" << i+1 << ": " <<  "Bad magician!" << endl;
		//ofs << "Case #" << i+1 << ": " <<  "Bad magician!" << endl;

	}

	//cout << "Case #" << data.lineNumber << ": " << output << endl;
	//ofs <<  "Case #" << data.lineNumber << ": " << output << endl;
}

void MainFunc( ifstream& ifs ,  ofstream& ofs )
{
	InputDataSet inputData;

	string lineBuf;
	vector<string> splittedLineBuf;
	vector<long> splittedLineNums;

	int lineCount = 0;
	int Tcount = 0;
	TestData testData;

	while(ifs) {
		splittedLineBuf.clear();
		lineBuf.clear();
		splittedLineNums.clear();

		if( !getline(ifs, lineBuf) ) {
			cout << "eof" << endl;
			break;
		}
		split( lineBuf , ' ' , splittedLineBuf );
		
		if( lineCount == 0 ) {
			Tcount = StringToNumber<int>( lineBuf );
			inputData.T = Tcount;
		}
		else {
			if( splittedLineBuf.size() < 3 ) {
				continue;
			}

			testData.R = StringToNumber<long>( splittedLineBuf[0] );
			testData.C= StringToNumber<long>( splittedLineBuf[1] );
			testData.M = StringToNumber<long>( splittedLineBuf[2] );
			
			inputData.vecData.push_back( testData );
			memset( &testData , 0 , sizeof(testData) );
		}

		lineCount++;
	}

	Calc( inputData , ofs );

}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc > 3 || argc == 1 ) {
		cout << "invalid args" << endl;
		return -1;
	}

	ifstream ifs( argv[1] );
	ofstream ofs( OUTPUT_FILENAME );

	MainFunc( ifs , ofs );

	ifs.close();
	ofs.close();

	cout << "enter any key ..." << endl;
	char in;
	cin.get(in);

	return 0;
}

