#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void getNums(char board[4][4], int row, char* rowNums)
{
	for(int i = 0; i < 4; i++)
	{
		rowNums[i] = board[row][i];
	}
}

int main(int argc, char *argv[])
{
	ifstream input(argv[1]);
	//input.open("test.txt");
	if(!input.is_open())
	{
		cout << "Error Opening";
		return 0;
	}
	int add;
	int total;
	input >> total;
	int board1Row;
	int board2Row;
	char board1[4][4];
	char board2[4][4];
	char board1Sol[4];
	char board2Sol[4];

	for(int count = 0; count < total; count++)
	{
		cout << "Case #" << count + 1 << ": ";
		input >> board1Row;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				input >> add;
				board1[i][j] = add;
			}
		}

		input >> board2Row;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				input >> add;
				board2[i][j] = add;
			}
		}

		getNums(board1, board1Row - 1, board1Sol);
		getNums(board2, board2Row - 1, board2Sol);

		int solution;
		bool match = false;
			
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(board1Sol[i] == board2Sol[j])
				{
					if(match == true)
					{
						cout << "Bad magician!";
						goto next;
					}
					solution = board1Sol[i];
					match = true;
				}
			}
		}

		if(match == false)
			cout << "Volunteer cheated!";
		else
			cout << solution;
		next:
		cout << endl;
	}
	return 0;
}