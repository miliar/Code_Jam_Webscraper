#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for (int s=0; s<t; s++)
    {
        char boardX[4][4];
        char boardO[4][4];
        bool fin = false;
        int ctrX = 0;
        int ctrO = 0;
        int ctrDot = 0;
        string str;
        getline(cin, str);
        for(int row=0; row<4; row++)
        {
            getline(cin, str);
            for(int col=0; col<4; col++)
            {
                if(str[col]=='X')
                {
                    if(str[col]=='X'){ctrX++;}
                    boardX[row][col]='X';
                    boardO[row][col]='.';
                }
                else if(str[col]=='O')
                {
                    if(str[col]=='O'){ctrO++;}
                    boardO[row][col]='O';
                    boardX[row][col]='.';
                }
                else if(str[col]=='T')
                {
                    boardX[row][col]='X';
                    boardO[row][col]='O';
                }
                else
                {
                    ctrDot++;
                    boardX[row][col] = '.';
                    boardO[row][col] = '.';
                }
            }
        }

        //cout << "jumlah X: " << ctrX << "\n";
        //cout << "jumlah O: " << ctrO << "\n";
        //cetakPapan(boardO);

        if(ctrX > ctrO)
        {
            //cekX
            //hor & ver
            int i=0;
            while(i<4 && fin==false)
            {
                if(boardX[i][0]=='X' && boardX[i][1]=='X' && boardX[i][2]=='X' && boardX[i][3]=='X')
                {
                    fin=true;
                    break;
                }
                if(boardX[0][i]=='X' && boardX[1][i]=='X' && boardX[2][i]=='X' && boardX[3][i]=='X')
                {
                    fin=true;
                    break;
                }
                i++;
            }
            if(fin==false)
            {
                if(boardX[0][0]=='X' && boardX[1][1]=='X' && boardX[2][2]=='X' && boardX[3][3]=='X')
                {
                    fin=true;
                }
                else if(boardX[0][3]=='X' && boardX[1][2]=='X' && boardX[2][1]=='X' && boardX[3][0]=='X')
                {
                    fin=true;
                }

                if (fin==false)
                {
                    //cek Draw
                    if (ctrDot == 0)
                    {
                        cout << "Case #" << (s+1) << ": Draw\n";
                    }
                    else
                    {
                        cout << "Case #" << (s+1) << ": Game has not completed\n";
                    }
                }
                else
                {
                    cout << "Case #" << (s+1) << ": X won\n";
                }
            }
            else
            {
                cout << "Case #" << (s+1) << ": X won\n";
            }
        }
        else
        {
            //cekO
            //hor & ver
            int i=0;
            while(i<4 && fin==false)
            {
                if(boardO[i][0]=='O' && boardO[i][1]=='O' && boardO[i][2]=='O' && boardO[i][3]=='O')
                {
                    fin=true;
                    break;
                }
                if(boardO[0][i]=='O' && boardO[1][i]=='O' && boardO[2][i]=='O' && boardO[3][i]=='O')
                {
                    fin=true;
                    break;
                }
                i++;
            }
            if(fin==false)
            {
                if(boardO[0][0]=='O' && boardO[1][1]=='O' && boardO[2][2]=='O' && boardO[3][3]=='O')
                {
                    fin=true;
                }
                else if(boardO[0][3]=='O' && boardO[1][2]=='O' && boardO[2][1]=='O' && boardO[3][0]=='O')
                {
                    fin=true;
                }

                if (fin==false)
                {
                    //cek Draw
                    if (ctrDot == 0)
                    {
                        cout << "Case #" << (s+1) << ": Draw\n";
                    }
                    else
                    {
                        cout << "Case #" << (s+1) << ": Game has not completed\n";
                    }
                }
                else
                {
                    cout << "Case #" << (s+1) << ": O won\n";
                }
            }
            else
            {
                cout << "Case #" << (s+1) << ": O won\n";
            }
        }
    }
    return 0;
}
