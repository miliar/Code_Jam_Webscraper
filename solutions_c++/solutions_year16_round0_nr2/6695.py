#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <list>
#include <algorithm>
#include <bitset>
#include <vector>

using namespace std;

const char* INPUT_FILE_NAME = "B-large.in";
const char* OUTPUT_FILE_NAME = "B-large.out";
//const char* INPUT_FILE_NAME  = "B-small-attempt0.in";
//const char* OUTPUT_FILE_NAME = "B-small-attempt0.out";
//const char* INPUT_FILE_NAME  = "B-small.in";
//const char* OUTPUT_FILE_NAME = "B-small.out";

int countFlip(const std::string& input)
{
	bool prev_up = (input[0] == '+');
	int count = 0;
	bool cur_up = prev_up;
	for (int i = 1; i < input.size(); ++i)
	{
		cur_up = (input[i] == '+');
		if (cur_up != prev_up)
		{
			++count;
		}
		prev_up = cur_up;
	}
	if (cur_up == false)
		++count;
	return count;
}

int main()
{
	int T;
	string strOutput;
	string strInput;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out | ios_base::trunc);
	outputFileStream.setf(ios_base::floatfield, ios_base::fixed);
	outputFileStream.precision(7);
	cout.setf(ios_base::floatfield, ios_base::fixed);
	cout.precision(7);

	inputFileStream >> T;

	for (int i = 0; i < T; ++i)
	{
		int sum_aud = 0;
		int added_aud = 0;

		string S;
		inputFileStream >> S;

		int result = countFlip(S);

		cout << "Case #" << i + 1 << ": ";
		outputFileStream << "Case #" << i + 1 << ": ";
		{
			cout << result;
			outputFileStream << result;
		}
		cout << endl;
		outputFileStream << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
