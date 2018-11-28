#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <set>
#include <list>
#include <cassert>
#include <memory>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int testCount = 0;

class InputReader
{
	fstream m_fileStream;
	char* m_pBuffer;
	static const int BufferSize = 1024 * 1024;

public:
	InputReader(const char* fileName)
		: m_fileStream(fileName)
	{
		if (!m_fileStream)
			throw "File not found!";

		m_pBuffer = new char[1024 * 1024];
	}

	~InputReader()
	{
		delete m_pBuffer;
		m_pBuffer = nullptr;
	}

	bool IsEof() const
	{
		return m_fileStream.eof();
	}

	string GetNextLine()
	{
		m_fileStream.getline(m_pBuffer, BufferSize);
		return string(m_pBuffer);
	}
};

int ReadNumberFromLine(const string& line)
{
	return atoi(line.c_str());
}

const int BoardSize = 4;

// returns the winner (X or O) or \0 if no winner
char GetWinner(string line)
{
	int count_T = count(line.begin(), line.end(), 'T');
	int count_O = count(line.begin(), line.end(), 'O') + count_T;

	if (count_O == BoardSize)
		return 'O';

	int count_X = count(line.begin(), line.end(), 'X') + count_T;

	if (count_X == BoardSize)
		return 'X';

	return '\0';
}

bool HasWinner(char winner)
{
	if (winner == '\0')
		return false;

	cout << winner << " won" << endl;
	return true;
}

void Solve(int caseNumber, const vector<string>& board)
{
	cout << "Case #" << caseNumber << ": ";

	bool hasEmptySpace = false;

	// search foir winner in rows
	for (size_t iLine = 0; iLine < board.size(); iLine++)
	{
		string line = board[iLine];
		if (line.size() != BoardSize)
			throw "Invalid line size";

		// search for empty cell
		if (line.find('.') != line.npos)
			hasEmptySpace = true;

		// search for winner
		auto winner = GetWinner(line);
		if (HasWinner(winner))
			return;		
	}

	// search foir winner in columns
	for (size_t iColumn = 0; iColumn < BoardSize; iColumn++)
	{
		string line;
		line += board[0][iColumn];
		line += board[1][iColumn];
		line += board[2][iColumn];
		line += board[3][iColumn];

		// search for winner
		auto winner = GetWinner(line);
		if (HasWinner(winner))
			return;		
	}

	// search for winner in diagonal 1
	{
		string line;
		for (size_t i = 0; i < BoardSize; i++)
			line += board[i][i];

		// search for winner
		auto winner = GetWinner(line);
		if (HasWinner(winner))
			return;		
	}

	// search for winner in diagonal 2
	{
		string line;
		for (size_t i = 0; i < BoardSize; i++)
			line += board[i][3 - i];

		// search for winner
		auto winner = GetWinner(line);
		if (HasWinner(winner))
			return;		
	}

	if (hasEmptySpace)
	{
		cout << "Game has not completed" << endl;
		return;
	}

	cout << "Draw" << endl;
}

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		cout << "must inform the file name in the command line" << endl;
		return -1;
	}
	
	InputReader reader(argv[1]);

	string line = reader.GetNextLine();
	int testCount = ReadNumberFromLine(line);

	for (int i = 0; i < testCount; i++)
	{
		vector<string> board;
		for (int iLine = 0; iLine < BoardSize; iLine++)
			board.push_back(reader.GetNextLine());

		Solve(i + 1, board);

		// reads the blank line
		line = reader.GetNextLine();
	}

	return 0;
}
