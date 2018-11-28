// StandingOvation.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#ifdef _UNICODE
	typedef std::wstring _tstring;
	typedef std::wstringstream _tstringstream;
#else
	typedef std::string _tstring;
	typedef std::stringstream _tstringstream;
#endif

using namespace std;

void Answer1( ofstream& ofs, int index, int maxShynessLevel, const string& strDigits );

int _tmain(int argc, _TCHAR* argv[])
{
	_tstring inPath = _T("C:\\dev\\GoogleCodeJam\\2015StandingOvation\\data\\input.txt");
	_tstring outPath = _T("C:\\dev\\GoogleCodeJam\\2015StandingOvation\\data\\output.txt");

//	ofstream tmp( outPath.c_str(), ios::out );
//	Answer1( tmp, 0, 0, "1" );

	ifstream ifs( inPath.c_str() );
	if( ifs.is_open() == false )
	{
		cout << _T("inPath open error.") << endl << inPath.c_str() << endl;
		getchar();
		return 0;
	}

	ofstream ofs( outPath.c_str(), ios::out );
	if( ofs.is_open() == false )
	{
		cout << _T("outPath open error.") << endl << outPath.c_str() << endl;
		getchar();
		return 0;
	}

	int numCases;
	ifs >> numCases;

	for( int i = 0; i < numCases; i++ )
	{
		int  maxShynessLevel;
		string strDigits;
		ifs >> maxShynessLevel;
		ifs >> strDigits;

		Answer1( ofs, i + 1, maxShynessLevel, strDigits );
	}

	cout << "done." << endl;
	getchar();

	return 0;
}

void Answer1( ofstream& ofs, int index, int maxShynessLevel, const string& strDigits )
{
	int requiredFriendsCount = 0;
	int curr = 0;
	for( int i = 0; i < maxShynessLevel + 1; i++ )
	{
		char strDigit = strDigits[ i ];
		int n = atoi( &strDigit );

		if( 0 < n )
		{
			if( curr < i )
			{
				requiredFriendsCount += i - curr;
				curr += i - curr;
			}
			curr += n;
		}
	}

	ofs << "Case #" << index << ": " << requiredFriendsCount << endl;
}

