#include <cstdio>

#define X_Won   1
#define O_Won   2
#define Draw    0
#define Incmp   3

int abs(int x)
{
    return x < 0 ? (-x) : x;
}

void print_status(int status)
{
    switch (status)
    {
        case X_Won:
            printf("X won");
            break;
        case O_Won:
            printf("O won");
            break;
        case Draw:
            printf("Draw");
            break;
        case Incmp:
            printf("Game has not completed");
            break;
    }
}

int main()
{
    int T, k = 1, status, i, j;
    char board[5][5];
    int decode[256];
    
    int points_row, points_col;
    int points_diag[2];
    
    decode['X'] = 1;   decode['O'] = -1;
    decode['.'] = 0;   decode['T'] = 10;
    
    scanf("%d", &T);
    while (T--)
    {
        status = Draw;
        
        for (i = 0; i < 4; ++i)
            scanf("%s", board[i]);
        
        for (i = 0; i < 4; ++i)
        {
            points_row = points_col = 0;
            for (j = 0; j < 4; ++j)
            {
                if (status == Draw  &&
                        (board[i][j] == '.'  ||
                         board[j][i] == '.'))
                    status = Incmp;
                
                points_row += decode[ board[i][j] ];
                points_col += decode[ board[j][i] ];
            }
            
            if (points_row == 7)
                points_row -= (decode['T'] + 1);
			else if (points_row == 13)
				points_row -= (decode['T'] - 1);
                
            if (points_col == 7)
                points_col -= (decode['T'] + 1);
			else if (points_col == 13)
                points_col -= (decode['T'] - 1);
            
            if (abs(points_row) == 4)
            {
                status = points_row > 0 ? X_Won : O_Won;
                break;
            }
            
            if (abs(points_col) == 4)
            {
                status = points_col > 0 ? X_Won : O_Won;
                break;
            }
        }
        
        if (status == Draw  ||  status == Incmp)
        {
            points_diag[0] = points_diag[1] = 0;
            for (i = 0; i < 4; ++i)
            {
                points_diag[0] += decode[ board[i][i] ];
                points_diag[1] += decode[ board[i][3 - i] ];
            }
            
            for (i = 0; i < 2; ++i)
            {
                if (points_diag[i] == 7)
					points_diag[i] -= (decode['T'] + 1);
				else if (points_diag[i] == 13)
					points_diag[i] -= (decode['T'] - 1);
				
                if (abs(points_diag[i]) == 4)
                {
                    status = points_diag[i] > 0 ? X_Won : O_Won;
                    break;
                }
            }
        }
        
        printf("Case #%d: ", k);
        print_status(status);
        printf("\n");
        k++;
    }
    
    return 0;
}
