#include<stdio.h>
#include<stdlib.h>

bool check_row(char **board, char p)
{
    for(int i=0; i<4; i++)
    {
        bool t = false;
        int player_count = 0;
        for(int j=0; j<4; j++)
        {
            if(board[i][j] == 'T')
                t = true;
            else if(board[i][j] == p)
                player_count++;
        }
        if(player_count == 4 || (player_count==3 && t))
            return true;
    }
    return false;
}

bool check_col(char **board, char p)
{
    for(int j=0; j<4; j++)
    {
        bool t = false;
        int player_count = 0;
        for(int i=0; i<4; i++)
        {
            if(board[i][j] == 'T')
                t = true;
            else if(board[i][j] == p)
                player_count++;
        }
        if(player_count == 4 || (player_count==3 && t))
            return true;
    }
    return false;
}

bool check_dia(char **board, char p)
{
    bool t;
    int player_count;
    // checking diagonal 1
    t = false;
    player_count = 0;
    for(int i=0; i<4; i++)
    {
        if(board[i][i] == 'T')
            t = true;
        else if(board[i][i] == p)
            player_count++;
    }
    if(player_count == 4 || (player_count == 3 && t))
        return true;

    // check diagonal 2
    t = false;
    player_count = 0;
    for(int i=0; i<4; i++)
    {
        if(board[i][3-i] == 'T')
            t = true;
        else if(board[i][3-i] == p)
            player_count++;
    }
    if(player_count == 4 || (player_count == 3 && t))
        return true;

    return false;
}

bool check_draw(char **board)
{
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if(board[i][j] == '.')
                return false;
        }
    }
    return true;
}

void check(char **board, int caseno)
{
    // checking for X wins
    if(check_row(board, 'X') || check_col(board, 'X') || check_dia(board, 'X'))
        printf("Case #%d: X won\n", caseno);
    else if(check_row(board, 'O') || check_col(board, 'O') || check_dia(board, 'O'))
        printf("Case #%d: O won\n", caseno);
    else if(check_draw(board))
        printf("Case #%d: Draw\n", caseno);
    else
        printf("Case #%d: Game has not completed\n", caseno);

}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, caseno = 1;
    scanf("%d", &t);
//    printf("t= %d\n", t);
    getchar();
    while(t--)
    {

        char **board = (char**)malloc(4 * sizeof(char*));
        for(int i=0; i<4; i++)
            board[i] = (char*)malloc(4 * sizeof(char));
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                scanf("%c", &board[i][j]);
            }
            getchar();
        }
        check(board, caseno);
        caseno++;
        getchar();
    }
    return 0;
}
