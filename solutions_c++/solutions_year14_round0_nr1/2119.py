#include <iostream>
#include <fstream>
using namespace std;

class MagicianProblem
{
private:
	int FirstBoard[4][4], SecondBoard[4][4];
	int FirstRow, SecondRow;
	int Result;
public:
	void ReadInput(fstream &f)
	{
		f >> FirstRow;
		FirstRow--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				f >> FirstBoard[i][j];
		f >> SecondRow;
		SecondRow--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				f >> SecondBoard[i][j];
	}
	void Solve()
	{
		int flag = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (FirstBoard[FirstRow][i] == SecondBoard[SecondRow][j])
				{
					Result = FirstBoard[FirstRow][i];
					flag ++;
				}
			}
			if (flag == 2)
				break;
		}
		if (flag == 0)
			Result = -1;
		else if (flag != 1)
			Result = -2;
	}
	void WriteOuput(int nTestCase, fstream &f)
	{
		f << "Case #" << nTestCase << ": ";
		if (Result == -1)
			f << "Volunteer cheated!";
		else if (Result == -2)
			f << "Bad magician!";
		else 
			f << Result;
		f << endl;
	}
};

int main(int argc, char **argv)
{
	fstream input, output;
	input.open(argv[1], ios::in);
	output.open(argv[2], ios::out);
	int nTestCase;
	input >> nTestCase;
	MagicianProblem MP;
	for (int i = 0; i < nTestCase; i++)
	{
		MP.ReadInput(input);
		MP.Solve();
		MP.WriteOuput(i + 1, output);
	}
	input.close();
	output.close();
	return 0;
}