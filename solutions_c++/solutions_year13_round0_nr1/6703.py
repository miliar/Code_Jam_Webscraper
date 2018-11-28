/*

    Codejam 2013
    Problem A. Tic-Tac-Toe-Tomek

*/

#include <stdio.h>
#include <string>
using namespace std ;

FILE *in = fopen("input.in", "r") ;
FILE *out = fopen("input.out", "w") ;

int main()
{
    int i, j, k, l ;
    int N ;
    char board[5][5] ;
    int x, o, T, ans ;

    fscanf(in, "%d\n", &N) ;
    for(l=1;l<=N;l++)
    {
        ans = 0 ;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(in, "%c", &board[i][j]) ;
                if( board[i][j] == '.' ) ans = 3 ;
            }
            fscanf(in, "\n") ;
        }
        fscanf(in, "\n") ;

        for(i=0;i<4;i++)
        {
            x = 0 ;
            o = 0 ;
            T = 0 ;
            for(j=0;j<4;j++)
            {
                if( board[i][j] == 'X' ) x ++ ;
                if( board[i][j] == 'O' ) o ++ ;
                if( board[i][j] == 'T' ) T ++ ;
            }
            if( x == 4 || (x == 3 && T == 1) ) ans = 1 ;
            if( o == 4 || (o == 3 && T == 1) ) ans = 2 ;
        }

        for(j=0;j<4;j++)
        {
            x = 0 ;
            o = 0 ;
            T = 0 ;
            for(i=0;i<4;i++)
            {
                if( board[i][j] == 'X' ) x ++ ;
                if( board[i][j] == 'O' ) o ++ ;
                if( board[i][j] == 'T' ) T ++ ;
            }
            if( x == 4 || (x == 3 && T == 1) ) ans = 1 ;
            if( o == 4 || (o == 3 && T == 1) ) ans = 2 ;
        }

        x = 0 ;
        o = 0 ;
        T = 0 ;
        for(i=0;i<4;i++)
        {
            if( board[i][i] == 'X' ) x ++ ;
            if( board[i][i] == 'O' ) o ++ ;
            if( board[i][i] == 'T' ) T ++ ;
        }
        if( x == 4 || (x == 3 && T == 1) ) ans = 1 ;
        if( o == 4 || (o == 3 && T == 1) ) ans = 2 ;

        x = 0 ;
        o = 0 ;
        T = 0 ;
        for(i=0;i<4;i++)
        {
            if( board[i][3-i] == 'X' ) x ++ ;
            if( board[i][3-i] == 'O' ) o ++ ;
            if( board[i][3-i] == 'T' ) T ++ ;
        }
        if( x == 4 || (x == 3 && T == 1) ) ans = 1 ;
        if( o == 4 || (o == 3 && T == 1) ) ans = 2 ;

        fprintf(out, "Case #%d: ", l) ;
        if( ans == 3 ) fprintf(out, "Game has not completed\n") ;
        if( ans == 0 ) fprintf(out, "Draw\n") ;
        if( ans == 1 ) fprintf(out, "X won\n") ;
        if( ans == 2 ) fprintf(out, "O won\n") ;
    }


    return 0 ;
}
