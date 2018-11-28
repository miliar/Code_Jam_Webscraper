#include <cstdio>
#include <cstring>
#include <assert.h>
#include <exception>

enum result{ X_WON=0, O_WON,DRAW=1, NOT_COMPLETED=2, NONE=4 };

class win : public std::exception{};
class x_win : public win
{
	virtual const char* what() const throw()
	{
		return "X won";
	}
};

class o_win : public win
{
	virtual const char* what() const throw()
	{
		return "O won";
	}
};

void parse_input(void);

enum result check_cells(char *board, int cell, int step);
void check_board(char * board);

void parse_input(void)
{
	int N, i;
	char board[16];
	scanf("%d\n", &N);
	for(i=0;i<N; i++)
	{
		memset(board, ' ', 16);
		scanf("%s\n", board);
		scanf("%s\n", board+4);
		scanf("%s\n", board+8);
		scanf("%s\n\n", board+12);

		printf("Case #%d: ", i+1);
		check_board(board);
	}
}

void check_board(char * board)
{
	int i,ret=0;
	try{
		for(i=0; i<4; i++)
			ret |= check_cells(board, i*4, 1);
		for(i=0;i<4; i++)
			ret |= check_cells(board, i, 4);
		ret |=check_cells(board, 0, 5);
		ret |=check_cells(board, 3, 3);
	}
	catch(win & e)
	{
		printf("%s\n", e.what());
		return;
	}
	if(ret & 0x2)
	{
		printf("Game has not completed\n");
		return;
	}
	if(ret & 0x4)
	{
		printf("Draw\n");
		return;
	}
	if(ret & 0x1)
		assert(0);
}
	
enum result check_cells(char *board, int cell, int step)
{
	int i;
	char * p= board + cell;
	char tmp='\0';

	for(i=0;i<4;i++)
	{
		if(*p == '.')
			return NOT_COMPLETED;
		if(tmp=='\0' && *p != 'T')
			tmp=*p;
		else if(tmp != *p && tmp != '\0' && *p!='T')
			return NONE;
		p += step;
	}

	if(tmp == 'X')
		throw x_win();
	else if(tmp == 'O')
		throw o_win();
	else assert(0);
}

int main(void)
{
	parse_input();
	return 0;
}

