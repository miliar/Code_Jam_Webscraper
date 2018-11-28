#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <list>
#include <algorithm>
#include <bitset>
#include <vector>

using namespace std;

const char* INPUT_FILE_NAME = "A-large.in";
const char* OUTPUT_FILE_NAME = "A-large.out";
//const char* INPUT_FILE_NAME  = "A-small-attempt0.in";
//const char* OUTPUT_FILE_NAME = "A-small-attempt0.out";
//const char* INPUT_FILE_NAME  = "A-small.in";
//const char* OUTPUT_FILE_NAME = "A-small.out";

int countSheep(int seed)
{
	if (seed == 0)
		return -1;
	const int goal = 1023;
	int appearance = 0;

	int cur = seed;
	while (true)
	{
		int p = cur;
		do
		{
			int d = p % 10;
			appearance |= (1 << d);
			p /= 10;
		} while (p > 0);

		if (appearance == goal)
			break;

		cur += seed;
	} 
	return cur;
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

		int N;
		inputFileStream >> N;

		int result = countSheep(N);

		cout << "Case #" << i + 1 << ": ";
		outputFileStream << "Case #" << i + 1 << ": ";
		if (result == -1)
		{
			cout << "INSOMNIA";
			outputFileStream << "INSOMNIA";
		}
		else
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
