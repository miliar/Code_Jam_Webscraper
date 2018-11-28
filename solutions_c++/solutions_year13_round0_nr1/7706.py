
#include<fstream>
#include<string>

using namespace std;


enum Result
{
	Xwon,
	Owon,
	Draw,
	NotCompleted,
	Unknown
};

bool anyDot = false;

Result checkLine(char line[4])
{
	Result result = Unknown;
	int OCount = 0;
	bool isDot = false;
	bool isT = false;
	for(int i = 0; i < 4; i++)
	{
		char ch = line[i];
		if(ch == 'O')
			OCount++;
		else if(ch == 'T')
			isT = true;
		else if(ch == '.')
			isDot = true;
	}
	if(OCount == 4 || OCount == 3 && isT == true)
	{
		result = Owon;
	}
	else if(OCount == 0 && isDot == false)
	{
		result = Xwon;
	}
	anyDot = anyDot | isDot;
	return result;
}

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int testCases;
	in >> testCases;

	for(int caseNumber = 0; caseNumber < testCases; caseNumber++)
	{
		anyDot = false;
		char board[4][4];
		Result result = Unknown;
		for(int row = 0; row < 4; row++)
		{
			for(int column = 0; column < 4; column++)
			{
				in >> board[row][column];
			}
		}

		for(int row = 0; row < 4 && result == Unknown; row++)
		{
			char rowLine[4];
			for(int column = 0; column < 4; column++)
			{
				rowLine[column] = board[row][column];
			}
			result = checkLine(rowLine);
		}

		for(int column = 0; column < 4 && result == Unknown; column++)
		{
			char columnLine[4];
			for(int row = 0; row < 4; row++)
			{
				columnLine[row] = board[row][column];
			}
			result = checkLine(columnLine);
		}

		for(int lineNr = 0; lineNr < 2 && result == Unknown; lineNr++)
		{
			char diagonalLine[4];
			for(int i = 0; i < 4; i++)
			{
				if(lineNr == 0)
					diagonalLine[i] = board[i][i];
				else
					diagonalLine[i] = board[i][3 - i];
			}
			result = checkLine(diagonalLine);
		}

		string resultText;
		if(result == Owon)
		{
			resultText = "O won";
		}
		else if(result == Xwon)
		{
			resultText = "X won";
		}
		else if(result == Unknown && anyDot)
		{
			resultText = "Game has not completed";
		}
		else
		{
			resultText = "Draw";
		}

		out << "Case #" << caseNumber + 1 << ": " << resultText << endl;
	}

	return 0;
}
