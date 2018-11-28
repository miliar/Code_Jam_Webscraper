#include <iostream>
#include <fstream>

using namespace std;

int iCaseNo = -1;
int r = -1;
int t = -1;
int iNoBlackRings = -1;

ifstream fin ("C:/Users/SHERMAL/Desktop/A-small-attempt0.in");
ofstream fout ("C:/Users/SHERMAL/Desktop/out.txt");

void Init();
void ReadInput();
void Process();
void Print();

int main(int argc, char* argv[])
{
	if (fin.is_open())
	{
		Init();

		fin.close();
	}

	fout.close();

    return 0;
}

void Init()
{
	int iT = 0;
	fin >> iT;

	iCaseNo = 0;

	
	while ( iT > 0 )
	{
		iT--;
		iCaseNo++;

		ReadInput();

		Process();

		Print();
	}
}

void ReadInput()
{
	fin >> r;
	fin >> t;
}

void Process()
{
	int fUsedPaint = 0;

	iNoBlackRings = 0;

	while ( fUsedPaint <= t )
	{
		

		int iInner = r;

		++r;

		int iOuter = r;

		++r;

		fUsedPaint = fUsedPaint +  ( ( iOuter   - iInner ) * ( iOuter   +  iInner ) );

		iNoBlackRings++;
	}

	iNoBlackRings--;
}

void Print()
{
		fout << "Case #" << iCaseNo << ": " << iNoBlackRings << endl;
}

