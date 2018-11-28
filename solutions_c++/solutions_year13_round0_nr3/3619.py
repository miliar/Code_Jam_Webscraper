#include <fstream>
#include <math.h>

using namespace std;

ifstream f_In ("C:/Users/SHERMAL/Desktop/C-small-attempt0.in");
ofstream f_Out ("C:/Users/SHERMAL/Desktop/out.txt");
  
void init();
bool IsPal(int iArg);

int main(int argc, char* argv[])
{
	
	if (f_In.is_open())
	{

		init();
		f_In.close();
	}

	f_Out.close();

	return 0;
}

void init(){
	int iT;
	int iLow;
	int iHigh;
	int iCaseNo = 0;

	f_In >> iT;

	while (iT > 0)
	{

		--iT;
		++iCaseNo;

		f_In >> iLow;
		f_In >> iHigh;

		int iSqrt = pow (iLow, 0.5);
		int iVal = iSqrt * iSqrt;
		int iCount = 0;

		if ( iVal < iLow )
		{
			++iSqrt;
			iVal = iSqrt * iSqrt;
		}

		while ( iVal <= iHigh )
		{
			

			if ( IsPal(iVal) && IsPal(iSqrt) )
			{
				++iCount;
			}

			++iSqrt;
			iVal = iSqrt * iSqrt;
		}

		f_Out << "Case #" << iCaseNo << ": " << iCount << endl;
	

	}
}

bool IsPal(int iArg)
{
	char buffer [200];
	int iNo;
	int iLeft = 0;
	int iRight;

	iNo=sprintf (buffer, "%d", iArg);

	iRight = iNo - 1;

	while ( iLeft < iRight )
	{
		if ( buffer[iLeft] != buffer[iRight] )
		{
			return false;
		}

		++iLeft;
		--iRight;
	}
	return true;
}


