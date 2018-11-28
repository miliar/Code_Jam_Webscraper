#include <iostream>
#include <fstream>

using namespace std;

#define BUF_SIZE 100
#define PICK_SIZE 4
char inBuf[BUF_SIZE];
ifstream inFile("A-small-attempt2.in");
ofstream outFile("result.out");

void ReadPick(int vPick[])
{
	inFile.getline(inBuf, BUF_SIZE);
	int nLine = atoi(inBuf);
	char* ptr;

	for ( int i = 1; i <= PICK_SIZE; ++i )
	{
		inFile.getline(inBuf, BUF_SIZE);
		if ( nLine != i ) continue;
    	
		sscanf( inBuf, "%d %d %d %d", &vPick[0], &vPick[1], &vPick[2], &vPick[3] );    
	}
}

void TestCase( int nCount )
{
	int Pick1[PICK_SIZE];
	int Pick2[PICK_SIZE];

	for ( int t = 0; t < nCount; ++t )
	{
		ReadPick(Pick1);
		ReadPick(Pick2);
	
		int nMatchCount = 0;
		int nPickNum = 0;
		for ( int i = 0; i < PICK_SIZE ;++i )
		{
			for ( int j = 0; j < PICK_SIZE; ++j )
			{
				if ( Pick1[i] == Pick2[j] ) 
				{
					++nMatchCount;
					nPickNum = Pick1[i];
				}
			}
		}
	
		string retStr;
		if ( nMatchCount == 0 )
		{
			outFile << "Case #" << t+1 << ": " << "Volunteer cheated!" << endl;
		}
		else if ( nMatchCount != 1 )
		{
			outFile << "Case #" << t+1 << ": " << "Bad magician!" << endl;
		}
		else
		{
			outFile << "Case #" << t+1 << ": " << nPickNum << endl;
		}
	}
}

int main(int argc, const char * argv[])
{
    inFile.getline(inBuf, BUF_SIZE);
    int nCount = atoi(inBuf);

	TestCase( nCount );	
	inFile.close();
    
    return 0;
}

