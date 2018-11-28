#include<iostream>
#include<fstream>
#include<cassert>
#include<string>

void checkBoard(char board[][4]);
int checkRow(char c1,char c2,char c3,char c4);


int main(int argc,char** argv)
{
	std::ifstream in(argv[1]);
	//std::ifstream in("input.txt");
	assert(in.is_open());
	std::string str;
	int numOfBoards = 0;

	char board[4][4];

	in >> numOfBoards;
	for(int i=0;i<numOfBoards;i++)
	{
		for(int j=0;j<4;j++)
		{
			in >>str;
			board[j][0] = str[0];
			board[j][1] = str[1];
			board[j][2] = str[2];
			board[j][3] = str[3];
		}
		std::cout<<"Case #"<<i+1<<": ";
		checkBoard(board);
		std::cout<<"\n";
		in.ignore();
	}
}

/*
0 - No Win No Blanks
1 - No Win Has Blanks
2 - X won
3 - O won
*/
void checkBoard(char board[][4])
{
	bool hasBlanks = false;
	int r=0;
	//Check horizontal
	for(unsigned short i=0;i<4;i++)
	{
		r = checkRow(board[0][i],board[1][i],board[2][i],board[3][i]);
		if(r == 2)
		{
			std::cout<<"X won";
			return;
		}
		if(r == 3)
		{
			std::cout<<"O won";
			return;
		}
		hasBlanks = (r == 0)?(hasBlanks):(true);
	}

	//Check vertical
	for(unsigned short i=0;i<4;i++)
	{
		r = checkRow(board[i][0],board[i][1],board[i][2],board[i][3]);
		if(r == 2)
		{
			std::cout<<"X won";
			return;
		}
		if(r == 3)
		{
			std::cout<<"O won";
			return;
		}
		hasBlanks = (r == 0)?(hasBlanks):(true);
	}

	//Check diagonal 1
	r = checkRow(board[0][0],board[1][1],board[2][2],board[3][3]);
	if(r == 2)
	{
		std::cout<<"X won";
		return;
	}
	if(r == 3)
	{
		std::cout<<"O won";
		return;
	}
	hasBlanks = (r == 0)?(hasBlanks):(true);

	//Check diagonal 2
	r = checkRow(board[0][3],board[1][2],board[2][1],board[3][0]);
	if(r == 2)
	{
		std::cout<<"X won";
		return;
	}
	if(r == 3)
	{
		std::cout<<"O won";
		return;
	}
	hasBlanks = (r == 0)?(hasBlanks):(true);

	//Draw or still in progress
	if(hasBlanks)
	{
		std::cout<<"Game has not completed";
		return;
	}
	else
		std::cout<<"Draw";
}

/*
returns--
0 - No Win No Blanks
1 - No Win Has Blanks
2 - X won
3 - O won
*/
int checkRow(char c1,char c2,char c3,char c4) 
{
	char c[4] = {c1,c2,c3,c4};
	int xCount = 0;
	int oCount = 0;
	int tCount = 0;
	int blankCount = 0;
	for(unsigned short i = 0;i<4;i++)
	{
		switch(c[i])
		{
		case 'X':
			xCount++;
			break;
		case 'O':
			oCount++;
			break;
		case 'T':
			tCount++;
			break;
		case '.':
			blankCount++;
			break;
		default:
			std::cerr<<"Bad Things!!!\n";
			break;
		}
	}
	
	//Check X
	if(xCount == 4)
		return 2;
	if(xCount == 3 && tCount == 1)
		return 2;

	//Check O
	if(oCount == 4)
		return 3;
	if(oCount == 3 && tCount == 1)
		return 3;

	//Check Blanks
	if(blankCount > 0)
		return 1;
	else
		return 0;
}