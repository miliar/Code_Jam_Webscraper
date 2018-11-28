#include <iostream>
#include <fstream>

using namespace std;

enum Result {notfind,hasfind, badMagic,cheat};

int main(int argc, char* argv[])
{
	int T;
	int ansA, ansB;
	int* squareA = new int[16];
	int* squareB = new int[16];

	ifstream input;
	ofstream output;
	input.open(argv[1], ios::in);
	output.open(argv[2], ios::out | ios::trunc);
	input >> T;

	for (int i = 1; i <= T; i++)
	{
		input >> ansA;
		ansA--;
		for (int j = 0; j < 16; j++)
			input >> squareA[j];
		input >> ansB;
		ansB--;
		for (int j = 0; j < 16; j++)
		{
			input >> squareB[j];
		}
		int result;
		Result finalResult=notfind;
		for (int j = 0; j < 4; j++)
		{
			int tmp = squareA[ansA * 4 + j];
			for (int k = 0; k < 4; k++)
			{
				if (tmp == squareB[ansB * 4 + k])
				{
					if (finalResult == notfind)
					{
						result = tmp;
						finalResult = hasfind;
						break;
					}
					else
					{
						if (finalResult == hasfind)
						{
							finalResult = badMagic;
							break;
						}
					}
				}
			}
			if (finalResult == badMagic)
				break;
		}
		switch (finalResult)
		{
		case notfind:
		{
						output << "Case #" << i << ": Volunteer cheated!" << endl;
						break;
		}
		case hasfind:
		{
						output << "Case #" << i << ": " << result << endl;
						break;
		}
		case badMagic:
		{
						 output << "Case #" << i << ": Bad magician!" << endl;
						 break;
		}
		default:
			break;
		}
		finalResult = notfind;
	}
	output.flush();
	output.close();
	input.close();
	delete[] squareA;
	delete[] squareB;
	return 0;
}