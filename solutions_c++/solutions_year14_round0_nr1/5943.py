#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;
const int kSize = 4;

void ReadArrange(ifstream& input, int board[][kSize])
{
	// read the board
	for (int i = 0; i < kSize; i++)
	{
		for (int j = 0; j < kSize; j++)
		{
			input >> board[i][j];
		}
		input.get();
	}
	return;
}

string CheckResult(int row_no1, int arrange1[][kSize], int row_no2, int arrange2[][kSize])
{
	int a;
	int b;
	int correct_num = 0;
	int result;
	ostringstream convert;
	for (int i = 0; i < kSize; i++)
	{
		a = arrange1[row_no1-1][i];
		for (int j = 0; j < kSize; j++)
		{
			b = arrange2[row_no2-1][j];
			if (a == b)
			{
				result = b;
				correct_num++;
				break;
			}
		}
	}
	if (correct_num == 0)
	{
		return "Volunteer cheated!";
	}
	else if (correct_num == 1)
	{
		convert << result;
		return convert.str();
	}
	else
	{
		return "Bad magician!";
	}
}

int main(void)
{
	int case_num;
	int row_no1;
	int row_no2;
	int arrange1[kSize][kSize];
	int arrange2[kSize][kSize];
	string result;
	ifstream input("A-small-attempt0.in");
	ofstream output("Result.out");

	input >> case_num;
	input.get();
	for (int i = 0; i < case_num; i++)
	{
		input >> row_no1;
		ReadArrange(input, arrange1);
		input >> row_no2;
		ReadArrange(input, arrange2);
		result = CheckResult(row_no1, arrange1, row_no2, arrange2);
		output << "Case #" << i + 1 << ": " << result << endl;
	}
	//output << board[0][0] << board[0][1] << endl;
	return 0;
}

