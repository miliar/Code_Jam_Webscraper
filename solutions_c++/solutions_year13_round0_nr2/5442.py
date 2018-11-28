#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool isTheSame(vector<int>& row)
{
	int curSmb = row[0];
	for (size_t i = 0; i < row.size(); i++)
	{
		if (curSmb != row[i])
		{
			return false;
		}
	}
	return true;
}

bool getResult(vector<vector<int>>& board, int maxHeight)
{
	vector<bool> theSameRows;
	vector<bool> theSameCols;

	//gather information about pattern
	size_t columnsCount = board[0].size();
	for (size_t col = 0; col < columnsCount; col++)
	{
		vector<int> curCol;
		for (size_t row = 0; row < board.size(); row++)
		{
			if (!col)
			{
				theSameRows.push_back(isTheSame(board[row]));
			}
			curCol.push_back(board[row][col]);
		}
		theSameCols.push_back(isTheSame(curCol));
	}

	//check if it's possible
	for (size_t row = 0; row < board.size(); row++)
	{
		vector<int>& curRow = board[row];
		for (size_t col = 0; col < curRow.size(); col++)
		{
			if (!theSameRows[row] && !theSameCols[col] && curRow[col] != maxHeight)
			{
				return false;
			}
		}
	}
	return true;
}

int main(int argc, char* argv[])
{
	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("data.dat");
	outputFile.open("data.res");
	if (inputFile.is_open() && outputFile.is_open())
	{
		int T;

		inputFile >> T;
		for (int t = 0; t < T; t++)
		{
			int N, M;
			inputFile >> N >> M;
			int maxHeight = 0;
			vector<vector<int>> board;
			for (int n = 0; n < N; n++)
			{
				vector<int> curRow;
				for (int m = 0; m < M; m++)
				{
					int curHeight;
					inputFile >> curHeight;
					if (curHeight > maxHeight)
					{
						maxHeight = curHeight;
					}
					curRow.push_back(curHeight);
				}
				board.push_back(curRow);
			}
			bool res = getResult(board, maxHeight);
			outputFile << "Case #" << (t + 1) << ": " << (res ? "YES" : "NO") << endl;
		}
	}
	inputFile.close();
	outputFile.close();
	return 0;
}