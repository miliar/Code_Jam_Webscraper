#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <list>
#include <algorithm>
#include <bitset>
#include <vector>

using namespace std;

const char* INPUT_FILE_NAME  = "A-large.in";
const char* OUTPUT_FILE_NAME = "A-large.out";
//const char* INPUT_FILE_NAME  = "A-small-attempt0.in";
//const char* OUTPUT_FILE_NAME = "A-small-attempt0.out";
//const char* INPUT_FILE_NAME  = "A-small.in";
//const char* OUTPUT_FILE_NAME = "A-small.out";

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
		int sum_aud = 0;
		int added_aud = 0;

		int S;
		inputFileStream >> S;

		string str;
		inputFileStream >> str;

		//cout << S << " " << str << endl;

		std::vector<int> audience(S + 1, 0);
		for (int j = 0; j <= S; ++j)
		{
			audience[j] = str[j] - '0';

			if (sum_aud < j)
			{
				int needed = j - sum_aud;
				sum_aud += needed;
				added_aud += needed;
			}

			sum_aud += audience[j];
		}

		cout << "Case #" << i + 1 << ": " << added_aud << endl;
		outputFileStream << "Case #" << i + 1 << ": " << added_aud << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
