#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <list>
#include <algorithm>
#include <bitset>
#include <vector>

using namespace std;

//const char* INPUT_FILE_NAME  = "D-large.in";
//const char* OUTPUT_FILE_NAME = "D-large.out";
const char* INPUT_FILE_NAME  = "D-small-attempt2.in";
const char* OUTPUT_FILE_NAME = "D-small-attempt2.out";
//const char* INPUT_FILE_NAME  = "D-small.in";
//const char* OUTPUT_FILE_NAME = "D-small.out";

int main()
{
	int T;
	string strOutput;
	string strInput;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out|ios_base::trunc);
	outputFileStream.setf(ios_base::floatfield, ios_base::fixed);
	outputFileStream.precision(7);
	cout.setf(ios_base::floatfield, ios_base::fixed);
	cout.precision(7);

	inputFileStream >> T;

	
	for (int i = 0; i < T; ++i)
	{
		int X, R, C;

		inputFileStream >> X >> R >> C;

		bool success = true;

		switch (X)
		{
		case 1:
			success = true;
			break;

		case 2:
			if (R % 2 == 1 && C % 2 == 1)
				success = false;
			break;

		case 3:
			if ((R == 2 && C == 3) ||
				(R == 3 && C == 2) ||
				(R == 4 && C == 3) ||
				(R == 3 && C == 4) ||
				(R == 3 && C == 3))
				success = true;
			else
				success = false;
			break;

		case 4:
			if ((R == 3 && C == 4) ||
				(R == 4 && C == 3) ||
				(R == 4 && C == 4))
				success = true;
			else
				success = false;
			break;

		default:
			success = false;
			break;
		}


		outputFileStream << "Case #" << i + 1 << ": " << (success ? "GABRIEL" : "RICHARD") << endl;

	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
