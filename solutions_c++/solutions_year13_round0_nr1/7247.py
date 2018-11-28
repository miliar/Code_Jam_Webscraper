#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<iostream>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<bitset>
#include<list>
using namespace std;

int main()
{
    freopen("E:\\A.in", "r", stdin);
    freopen("E:\\B.out", "w", stdout);
    char board[4][4];
    string str1;
    string str2;
    int T;
    scanf("%d", &T);
    getchar();

    for(int cas = 0; cas < T; cas++)
    {
        int X = 0, O = 0, T = 0, P = 0;

        for(int i = 0; i < 4; i++ )
        {
            for(int j = 0; j < 4; j++)
                scanf("%c", &board[i][j]);

            getchar();
        }

        for(int i = 0; i < 4; i++ )
        {
            for(int j = 0; j < 4; j++)
            {
                if(board[i][j] == 'X')
                    X++;
                else
                    if(board[i][j] == 'O')
                        O++;
                    else
                        if(board[i][j] == 'T')
                            T++;
                        else
                            if(board[i][j] == '.')
                                P++;
            }

            if((X + T) == 4 || (O + T) == 4)
                break;

            X = 0, O = 0, T = 0;
        }

        if((X + T) == 4 || (O + T) == 4)
        {

        }
        else
        {
            X = 0, O = 0, T = 0;

            for(int i = 0; i < 4; i++ )
            {
                for(int j = 0; j < 4; j++)
                {
                    if(board[j][i] == 'X')
                        X++;
                    else
                        if(board[j][i] == 'O')
                            O++;
                        else
                            if(board[j][i] == 'T')
                                T++;
                }

                if((X + T) == 4 || (O + T) == 4)
                    break;

                X = 0, O = 0, T = 0;
            }

            if((X + T) == 4 || (O + T) == 4)
            {

            }
            else
            {
                X = 0, O = 0, T = 0;

                for(int i = 0; i < 4; i++ )
                {
                    if(board[i][i] == 'X')
                        X++;
                    else
                        if(board[i][i] == 'O')
                            O++;
                        else
                            if(board[i][i] == 'T')
                                T++;

                }

                if((X + T) == 4 || (O + T) == 4)
                {

                }
                else
                {
                    X = 0, O = 0, T = 0;

                    for(int i = 0; i < 4; i++ )
                    {
                        if(board[i][3-i] == 'X')
                            X++;
                        else
                            if(board[i][3-i] == 'O')
                                O++;
                            else
                                if(board[i][3-i] == 'T')
                                    T++;

                    }
                }
            }

        }

        char *result = "";

        if((X + T) == 4)
        {
            result = "X won";
        }
        else
            if((O + T) == 4)
            {
                result = "O won";
            } else
                if(P > 0)
                {
                    result = "Game has not completed";
                }
                else {
                    result = "Draw";
                }

        printf("Case #%d: %s\n", cas + 1, result);
        getchar();
    }

    return 0;
}
