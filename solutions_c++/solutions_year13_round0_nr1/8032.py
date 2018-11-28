// takatak.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "memory.h"

typedef enum 
{
	GS_UNKNOWN,
	GS_X_WON,
	GS_O_WON,
	GS_DRAW
} GAME_STATE;

typedef struct {
	char col[4];
} ROW;

typedef struct {
	ROW row[4];
	GAME_STATE state;
	int t_row;
	int t_col;
	bool has_any_free_space;

	void check_row(int row_index)
	{
		if( state == GS_DRAW )
			return;

		ROW& r = row[row_index];
		if( row_index == t_row )
		{
			r.col[t_col] = 'X';
		}

		if( (r.col[0] == r.col[1]) &&
			(r.col[1] == r.col[2]) &&
			(r.col[2] == r.col[3]) )
		{
			if( r.col[0] == 'X' )
			{
				if( state == GS_O_WON )
				{
					//printf("draw in row %d\n", row_index);
					state = GS_DRAW;
					return;
				}
				else if( state == GS_UNKNOWN )
				{
					//printf("x won in row %d\n", row_index);
					state = GS_X_WON;
					return;
				}
			}
			else if( r.col[0] == 'O' )
			{
				if( state == GS_X_WON )
				{
					//printf("draw in row %d\n", row_index);
					state = GS_DRAW;
					return;
				}
				else if( state == GS_UNKNOWN )
				{
					//printf("o won in row %d\n", row_index);
					state = GS_O_WON;
					return;
				}
			}
		}

		if( row_index == t_row )
		{
			r.col[t_col] = 'O';

			if( (r.col[0] == r.col[1]) &&
				(r.col[1] == r.col[2]) &&
				(r.col[2] == r.col[3]) )
			{
				if( r.col[0] == 'O' )
				{
					if( state == GS_X_WON )
					{
						//printf("draw in row %d\n", row_index);
						state = GS_DRAW;
					}
					else if( state == GS_UNKNOWN )
					{
						//printf("o won in row %d\n", row_index);
						state = GS_O_WON;
					}
				}
			}
		}
	}

	void check_col(int col_index)
	{
		if( state == GS_DRAW )
			return;

		if( col_index == t_col )
		{
			row[t_row].col[t_col] = 'X';
		}

		if( (row[0].col[col_index] == row[1].col[col_index]) &&
			(row[1].col[col_index] == row[2].col[col_index]) &&
			(row[2].col[col_index] == row[3].col[col_index]) )
		{
			if( row[0].col[col_index] == 'X' )
			{
				if( state == GS_O_WON )
				{
					//printf("draw in col %d\n", col_index);
					state = GS_DRAW;
					return;
				}
				else if( state == GS_UNKNOWN )
				{
					//printf("x won in col %d\n", col_index);
					state = GS_X_WON;
					return;
				}
			}
			else if( row[0].col[col_index] == 'O' )
			{
				if( state == GS_X_WON )
				{
					//printf("draw in col %d\n", col_index);
					state = GS_DRAW;
					return;
				}
				else if( state == GS_UNKNOWN )
				{
					//printf("o won in col %d\n", col_index);
					state = GS_O_WON;
					return;
				}
			}
		}

		if( col_index == t_col )
		{
			row[t_row].col[t_col] = 'X';

			if( (row[0].col[col_index] == row[1].col[col_index]) &&
				(row[1].col[col_index] == row[2].col[col_index]) &&
				(row[2].col[col_index] == row[3].col[col_index]) )
			{
				if( row[0].col[col_index] == 'O' )
				{
					if( state == GS_X_WON )
					{
						//printf("draw in col %d\n", col_index);
						state = GS_DRAW;
					}
					else if( state == GS_UNKNOWN )
					{
						//printf("o won in col %d\n", col_index);
						state = GS_O_WON;
					}
				}
			}
		}
	}

	void check_diag(int x0, int y0, int x1, int y1, int x2, int y2, int x3, int y3)
	{
		if( state == GS_DRAW )
			return;

		row[t_row].col[t_col] = 'X';

		if( (row[x0].col[y0] == row[x1].col[y1]) &&
			(row[x1].col[y1] == row[x2].col[y2]) &&
			(row[x2].col[y2] == row[x3].col[y3]) )
		{
			if( row[x0].col[y0] == 'X' )
			{
				if( state == GS_O_WON )
				{
					//printf("draw in diag\n");
					state = GS_DRAW;
					return;
				}
				else if( state == GS_UNKNOWN )
				{
					//printf("x won in diag\n");
					state = GS_X_WON;
					return;
				}
			}
			else if( row[x0].col[y0] == 'O' )
			{
				if( state == GS_X_WON )
				{
					//printf("darw in diag\n");
					state = GS_DRAW;
					return;
				}
				else if( state == GS_UNKNOWN )
				{
					//printf("o won in diag\n");
					state = GS_O_WON;
					return;
				}
			}
		}

		row[t_row].col[t_col] = 'O';
		if( (row[x0].col[y0] == row[x1].col[y1]) &&
			(row[x1].col[y1] == row[x2].col[y2]) &&
			(row[x2].col[y2] == row[x3].col[y3]) )
		{
			if( row[x0].col[y0] == 'O' )
			{
				if( state == GS_X_WON )
				{
					//printf("draw in diag\n");
					state = GS_DRAW;
				}
				else if( state == GS_UNKNOWN )
				{
					//printf("o won in diag\n");
					state = GS_O_WON;
				}
			}
		}

	}

	void check_states()
	{
		state = GS_UNKNOWN;
		check_row(0);
		check_row(1);
		check_row(2);
		check_row(3);

		check_col(0);
		check_col(1);
		check_col(2);
		check_col(3);

		check_diag(0,0,1,1,2,2,3,3);
		check_diag(3,0,2,1,1,2,0,3);

		if( state == GS_UNKNOWN )
		{
			if( !has_any_free_space )
				state = GS_DRAW;
		}
	}

	void set_row(int n, const char* p)
	{
		if( n == 0 )
		{
			t_row = t_col = -1;
			has_any_free_space = false;
		}

		for( int i = 0; i < 4; ++i )
		{
			char c = p[i];
			row[n].col[i] = c;
			if( c == 'T' )
			{
				t_row = n;
				t_col = i;
			}
			else if( !has_any_free_space && (c != 'X') && (c != 'O') )
			{
				has_any_free_space = true;
			}
		}		
	}

} GAME;

class solver {

public:

	void process(const char* filename);
};

void solver::process(const char* filename)
{
	FILE* fp;
	fopen_s(&fp, filename, "r");
	static char line[10240];

	GAME g;
	int lno = 0;
	int recno = 0;
	int caseno = 1;
	while( !feof(fp) )
	{
		fgets(line, sizeof(line), fp);
		if( lno )
		{
			if( recno == 0 )
			{
				memset(&g, 0, sizeof(g));
			}
			if( recno < 4 )
			{
				g.set_row(recno++, line);
			}
			else if( recno == 4 )
			{
				static char* states[4] = 
				{
					"Game has not completed",
					"X won",
					"O won",
					"Draw"
				};
				g.check_states();

				printf("Case #%d: %s\n", caseno++, states[g.state]);
				recno = 0;
			}
		}
		++lno;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc == 2 )
		solver().process(argv[1]);
	else
		solver().process("C:\\A-small-attempt0.in");

	
	return 0;
}

