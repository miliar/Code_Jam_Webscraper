
#include "stdafx.h"

#include <stdlib.h>
#include <math.h>

#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iomanip>
#include <map>

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
	long long Smax;
	int Si[1000];
};

struct InputDataSet {
	int T;
	vector<TestData> vecData;
};

// Å‘åŒö–ñ”‚ğ‹‚ß‚éŠÖ”
long long gcd(long long a, long long b)
{
	while(a != b) {
		if (a < b) b -= a;
		else a-= b;
	}
	return a;
}

void Resolve( InputDataSet& data , ofstream& ofs ) 
{
	long long ca = 0;
	long add = 0;

	////cout << "Input (" << data.lineNumber << ") " << data.name << " n=" << data.n << endl;

	for( int i = 0; i < data.vecData.size() ; i++ ) {
		TestData test = data.vecData.at(i);
		
		//memset( ans , 0 , test.R*test.C );

		cout << "T:" << i 
			<< " Smax:" << test.Smax << " Si:";
		for( int ii = 0 ; ii <= test.Smax ; ii++ ) {
			cout << test.Si[ii];
		}
		cout << endl;

		ca = 0;
		add = 0;
		for( int ii = 0 ; ii <= test.Smax ; ii++ ) {
			cout << ca << " " << add  << " " << ii << endl;
			if(( test.Si[ii] > 0) && (ii > 0) ) {
				while( ii > (ca + add) ) {
					add++;
				}
			}
			ca += test.Si[ii];
		}
		
		cout << "Case #" << i+1 << ": " << add << endl;
		ofs << "Case #" << i+1 << ": " << add << endl;
		
	}



	//	long long max = 1LL << 40;

	//	long long yaku = 1;
	//	if( test.P <= 256 ) {
	//	//if( 0 ){
	//		for( int n = 256 ; n > 0 ; n-- ) {
	//			if( test.P % (long long)n == 0 ) {
	//				if( test.Q % (long long)n == 0 ) {
	//					yaku = n;
	//					break;
	//				}
	//			}
	//		}
	//	} 
	//	else {
	//		yaku = gcd( test.Q , test.P );
	//	}
	//	long long waru = test.Q;
	//	waru /= yaku;

	//	long long bunsi = test.P / yaku;

	//	long long rest = max % waru;

	//	cout << "max:" << max
	//		<< " yaku:" << yaku
	//		<< " waru:" << waru
	//		<< " Rest:" << rest 
	//		<< endl;

	//	if( rest != 0 ) {
	//		cout << "Case #" << i+1 << ": "
	//			<< "impossible"
	//			<< endl;
	//		ofs << "Case #" << i+1 << ": "
	//			<< "impossible"
	//			<< endl;
	//	}
	//	else {
	//		double pq = (double)bunsi / waru;
	//		cout << "pq:" << pq << endl;
	//		int resultGen = 0;
	//		for( int gen = 1 ; gen <= 40 ; gen++ ) {
	//			double testGen = 1.0 / (double)( 1LL << gen );
	//			if( pq >= testGen ) {
	//				resultGen = gen;
	//				break;
	//			}
	//		}
	//		cout << "Case #" << i+1 << ": "
	//			<< resultGen
	//			<< endl;
	//		ofs << "Case #" << i+1 << ": "
	//			<< resultGen
	//			<< endl;
	//	}

	//}

}

void ParseInput( ifstream& ifs ,  ofstream& ofs )
{
	InputDataSet inputData;

	string lineBuf;
	vector<string> splittedLineBuf;
	vector<long> splittedLineNums;

	int lineCount = 0;
	int Tcount = 0;
	TestData testData;
	TestData testDataEmpty = {};

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
			testData.Smax = StringToNumber<long long>( splittedLineBuf[0] );
			for( int i = 0 ; i <= testData.Smax ; i++ ) {
				string next;
				next += splittedLineBuf[1].at(i);
				testData.Si[i] = StringToNumber<int>( next );
				//cout << "input" << lineCount << ":" << testData.Si[i] << endl;
			}

			inputData.vecData.push_back( testData );
			testData = testDataEmpty;
		}

		lineCount++;
	}

	Resolve( inputData , ofs );

}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc > 3 || argc == 1 ) {
		cout << "invalid args" << endl;
		return -1;
	}

	ifstream ifs( argv[1] );
	ofstream ofs( OUTPUT_FILENAME );

	ParseInput( ifs , ofs );

	ifs.close();
	ofs.close();

	cout << "enter any key ..." << endl;
	char in;
	cin.get(in);

	return 0;
}

