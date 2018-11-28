#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    string board[4];
    int n, i, j, contX, contO;
    int caso = 1;

    scanf("%d",&n);

    while(n--)
    {
        cin >> board[0] >> board[1] >> board[2] >> board[3];

        int win=0;

        //Horizontal
        for(i=0; i<4; i++)
        {
            contO = contX = 0;
            for(j=0; j<4; j++)
            {
                if(board[i][j] == '.') win = 1;

                if(board[i][j] == 'X') { contX++; contO=0; }
                else if(board[i][j] == 'O') { contX = 0; contO++; }
                else if(board[i][j] == 'T') { contX++; contO++; }

                if(contX == 4) { win = 2; i = j = 5; }
                else if(contO == 4) { win = 3; i = j = 5; }
            }
        }

        //Vertical
        for(i=0; i<4; i++)
        {
            contO = contX = 0;
            for(j=0; j<4; j++)
            {
                if(board[j][i] == 'X') { contX++; contO=0; }
                else if(board[j][i] == 'O') { contX = 0; contO++; }
                else if(board[j][i] == 'T') { contX++; contO++; }

                if(contX == 4) { win = 2; i = j = 5; }
                else if(contO == 4) { win = 3; i = j = 5; }
            }
        }

        //Diagonal descendo
        contO = contX = 0;
        for(i=0, j=0; i<4 && j<4; i++, j++)
        {
            if(board[i][j] == 'X') { contX++; contO=0; }
            else if(board[i][j] == 'O') { contX = 0; contO++; }
            else if(board[i][j] == 'T') { contX++; contO++; }

            if(contX == 4) { win = 2; i = j = 5; }
            else if(contO == 4) { win = 3; i = j = 5; }
        }

        //Diagonal subindo
        contO = contX = 0;
        for(i=3, j=0; i>=0 && j<4; i--, j++)
        {
            if(board[i][j] == 'X') { contX++; contO=0; }
            else if(board[i][j] == 'O') { contX = 0; contO++; }
            else if(board[i][j] == 'T') { contX++; contO++; }

            if(contX == 4) { win = 2; i = j = 5; }
            else if(contO == 4) { win = 3; i = j = 5; }
        }

        printf("Case #%d: ",caso++);
        if(win == 0) printf("Draw\n");
        else if(win == 1) printf("Game has not completed\n");
        else if(win == 2) printf("X won\n");
        else if(win == 3) printf("O won\n");
    }

    return 0;
}
