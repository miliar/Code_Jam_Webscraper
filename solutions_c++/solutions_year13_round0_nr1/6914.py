#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <numeric>
#include <cctype>
#include <climits>
using namespace std;

typedef  vector< vector<char> > charmatr;

#define COLS (4)
#define ROWS (4)



bool go( int stpcol, int stprow, int col, int row, const charmatr& board, char ch )
{
	int matrsz = board.size();
	int count = 0;

	while( ( col < matrsz && row < matrsz && col >= 0 && row >= 0 ) ){
	    const char brdch = board[row][col];
		if( brdch == ch || brdch == 'T' )
			if( ++count == matrsz ){
				return true;
			}

		col += stpcol;
		row += stprow;

		if( col == COLS && stprow == 0 ){
			col = 0;
			count = 0;
			row++;
		}
		else
			if( row == ROWS && stpcol == 0 ){
				row = 0;
				count = 0;
				col++;
			}
	}

	return false;
}

bool check(const charmatr& board, char ch)
{
	bool rows = go( 1, 0, 0, 0, board, ch );
	bool cols = go( 0, 1, 0, 0, board, ch );
	bool diag1 = go( 1,1, 0, 0, board, ch );
	bool diag2 = go( -1,1, board.size()-1, 0, board, ch );

	return rows || cols || diag1 || diag2;
}

bool haveemptycell(const charmatr& board)
{
    for( int i = 0; i < COLS; i++ )
        for( int j = 0; j < ROWS; j++ )
            if( board[i][j] == '.' ){
                return true;
            }
    return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	charmatr  	board(COLS, vector<char>(ROWS));
	int ntests;
	scanf(" %d", &ntests);
	for( int test = 1; test <= ntests; ++test ) {
		printf("Case #%d: ", test);

		for( int i = 0; i < COLS; i++ )
			for( int j = 0; j < ROWS; j++ )
				scanf(" %c",&board[i][j]);

		bool Xwon = check( board, 'X' );
		bool Owon = check( board, 'O' );

		if( Xwon ){
			printf("X won\n");
		}
		else
			if( Owon ){
				printf("O won\n");
			}
			else
			    if(haveemptycell(board)){
			    	printf("Game has not completed\n");
                }
                else{
                    printf("Draw\n");
                }
	}
}
