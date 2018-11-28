#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int tc;
char board[4][4];

int main(){
    cin>>tc;
    for(int k=1;k<=tc;k++){
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>board[i][j];

        bool xwon, owon;
        int o,x,t,dot; //dot untuk seluruh board; o,x,t untuk baris/kolom/diagonal itu saja
        xwon = owon = false;
        dot = 0;
        //cek row
        for(int i=0;i<4;i++){
            o = x = t = 0;
            for(int j=0;j<4;j++)
                if(board[i][j] == 'O')
                    o++;
                else if(board[i][j] == 'X')
                    x++;
                else if(board[i][j] == 'T')
                    t++;
                else
                    dot++;
            if((o == 3 && t == 1) || (o == 4))
                owon = true;
            else if((x == 3 && t == 1) || (x == 4))
                xwon = true;
        }
        //cek col
        for(int j=0;j<4;j++){
            o = x = t = 0;
            for(int i=0;i<4;i++)
                if(board[i][j] == 'O')
                    o++;
                else if(board[i][j] == 'X')
                    x++;
                else if(board[i][j] == 'T')
                    t++;
                else
                    dot++;
            if((o == 3 && t == 1) || (o == 4))
                owon = true;
            else if((x == 3 && t == 1) || (x == 4))
                xwon = true;
        }
        //cek diagonal
        o = x = t = 0;
        for(int i=0;i<4;i++){
            if(board[i][i] == 'O')
                o++;
            else if(board[i][i] == 'X')
                x++;
            else if(board[i][i] == 'T')
                t++;
            else
                dot++;
        }
        if((o == 3 && t == 1) || (o == 4))
            owon = true;
        else if((x == 3 && t == 1) || (x == 4))
            xwon = true;

        o = x = t = 0;
        for(int i=0;i<4;i++){
            if(board[i][3 - i] == 'O')
                o++;
            else if(board[i][3 - i] == 'X')
                x++;
            else if(board[i][3 - i] == 'T')
                t++;
            else
                dot++;
        }
        if((o == 3 && t == 1) || (o == 4))
            owon = true;
        else if((x == 3 && t == 1) || (x == 4))
            xwon = true;

        cout<<"Case #"<<k<<": ";
        if(xwon && !owon)
            cout<<"X won\n";
        else if(owon && !xwon)
            cout<<"O won\n";
        else if(dot == 0)
            cout<<"Draw\n";
        else
            cout<<"Game has not completed\n";
    }
    return 0;
}
