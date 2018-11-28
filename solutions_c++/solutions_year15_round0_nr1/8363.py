#include <iostream>
#include <fstream>
#pragma warning(disable:4996)

using namespace std;

#define BUF_SIZE 1100

char inBuf[BUF_SIZE];
ifstream inFile("A-large.in");
ofstream outFile("result.out");

char lineBuf[BUF_SIZE];

int Logic()
{
	inFile.getline(inBuf, BUF_SIZE);

	int C;

	sscanf(inBuf, "%d %s", &C, &lineBuf);

	int result = 0;
	int audience = 0;

	for (int i = 0; i <= C; ++i)
	{
		int curAudience = lineBuf[i] - '0';
		if (curAudience > 0 &&  audience < i)
		{
			result += i - audience;
			curAudience += i - audience;
		}
		audience += curAudience;
	}

	return result;
}

void TestCase(int nCount)
{
	cout.precision(7);
	for (int i = 0; i < nCount; ++i)
	{
		int nResult = Logic();
		outFile << "Case #" << i + 1 << ": " << fixed << nResult << endl;
	}
}

int main()
{
	inFile.getline(inBuf, BUF_SIZE);
	int nCount = atoi(inBuf);

	TestCase(nCount);
	inFile.close();

	return 0;
}
