#include <stdio.h>

 int main() {

    int t, i, ii, ok, number = 1;
    char c;
    char board[10][10];

    scanf("%d", &t);

    while(t--)
    {
        ok = 0;
        for(i = 0; i < 4; i++)
        {
            getchar();
            for(ii = 0; ii < 4; ii++)
            {
                 scanf("%c", &c);
                 board[i][ii] = c;
                 if(c == '.') ok = 3;
            }
        }

        // player X
        for(i = 0; i < 4; i++)
        {
            if ( (board[i][0] == 'X' || board[i][0] == 'T')  &&
                 (board[i][1] == 'X' || board[i][1] == 'T')  &&
                 (board[i][2] == 'X' || board[i][2] == 'T')  &&
                 (board[i][3] == 'X' || board[i][3] == 'T')
               )
               ok = 1;
            if ( (board[0][i] == 'X' || board[0][i] == 'T')  &&
                 (board[1][i] == 'X' || board[1][i] == 'T')  &&
                 (board[2][i] == 'X' || board[2][i] == 'T')  &&
                 (board[3][i] == 'X' || board[3][i] == 'T')
               )
               ok = 1;
        }

        if ( (board[0][0] == 'X' || board[0][0] == 'T')  &&
             (board[1][1] == 'X' || board[1][1] == 'T')  &&
             (board[2][2] == 'X' || board[2][2] == 'T')  &&
             (board[3][3] == 'X' || board[3][3] == 'T')
           )
           ok = 1;
        if ( (board[3][0] == 'X' || board[3][0] == 'T')  &&
             (board[2][1] == 'X' || board[2][1] == 'T')  &&
             (board[1][2] == 'X' || board[1][2] == 'T')  &&
             (board[0][3] == 'X' || board[0][3] == 'T')
        )
           ok = 1;



        // player O
        for(i = 0; i < 4; i++)
        {
            if ( (board[i][0] == 'O' || board[i][0] == 'T')  &&
                 (board[i][1] == 'O' || board[i][1] == 'T')  &&
                 (board[i][2] == 'O' || board[i][2] == 'T')  &&
                 (board[i][3] == 'O' || board[i][3] == 'T')
               )
               ok = 2;
            if ( (board[0][i] == 'O' || board[0][i] == 'T')  &&
                 (board[1][i] == 'O' || board[1][i] == 'T')  &&
                 (board[2][i] == 'O' || board[2][i] == 'T')  &&
                 (board[3][i] == 'O' || board[3][i] == 'T')
               )
               ok = 2;
        }

        if ( (board[0][0] == 'O' || board[0][0] == 'T')  &&
             (board[1][1] == 'O' || board[1][1] == 'T')  &&
             (board[2][2] == 'O' || board[2][2] == 'T')  &&
             (board[3][3] == 'O' || board[3][3] == 'T')
           )
           ok = 2;
        if ( (board[3][0] == 'O' || board[3][0] == 'T')  &&
             (board[2][1] == 'O' || board[2][1] == 'T')  &&
             (board[1][2] == 'O' || board[1][2] == 'T')  &&
             (board[0][3] == 'O' || board[0][3] == 'T')
        )
           ok = 2;

        if(ok == 1)
            printf("Case #%d: X won\n", number++);
        if(ok == 2)
            printf("Case #%d: O won\n", number++);


        if(ok == 0)
            printf("Case #%d: Draw\n", number++);
        if(ok == 3)
            printf("Case #%d: Game has not completed\n", number++);

        getchar();
    }

    return 0;
 }
