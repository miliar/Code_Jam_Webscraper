#include <iostream>
#include <fstream>

using namespace std;

#define BUF_SIZE 100

char inBuf[BUF_SIZE];
ifstream inFile("B-large.in");
ofstream outFile("result.out");

double Cookie()
{
	inFile.getline( inBuf, BUF_SIZE );

	double C, F, X;
	sscanf( inBuf, "%lf %lf %lf", &C, &F, &X);
	
	int nStep = 0;
	double fResult = 0.0f;
	while( true )
	{
		double nextStep = C / ( 2.0 + F * nStep );
		double nextfinalStep = X / ( 2.0 + F * ( nStep + 1 ) );
		double finalStep = X / ( 2.0 + F * nStep );

		if ( ( nextStep + nextfinalStep ) > finalStep )
		{
			fResult += finalStep;
			break;
		}
		fResult += nextStep; 
		nStep++;
	}
	
	return fResult; 
}

void TestCase( int nCount )
{
	cout.precision(7);
	for ( int i = 0; i < nCount; ++i )
	{
		double nResult = Cookie();
		outFile << "Case #" << i + 1 << ": " << fixed << nResult << endl;
	}
}

int main()
{
	inFile.getline( inBuf, BUF_SIZE );
	int nCount = atoi( inBuf );

	TestCase( nCount );
	inFile.close();

	return 0;
}
