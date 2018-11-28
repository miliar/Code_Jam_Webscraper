#include <iostream>
#include <fstream>
using namespace std;
char game[4][4];
int empty=0;
enum{notCompleted, draw, Xwin, Owin};
int checkV()
{
    int X=0,O=0,T=0;
    bool isX=false,isO=false;
    for(int i=0;i<4;i++)
    {
        X=0;O=0;
        for(int j=0;j<4;j++)
        {
            switch(game[i][j])
            {
                case 'O':
                    O++;
                    break;
                case 'T':
                    O++;
                    X++;
                    break;
                case 'X':
                    X++;
                    break;
                case '.':
                    empty++;
            }
        }
        if(X==4)
            isX=true;
        if(O==4)
            isO=true;
    }
    if(isX && isO)
        return draw;
    if(isX)
        return Xwin;
    if(isO)
        return Owin;
    return notCompleted;
}
int checkH()
{
    int X=0,O=0,T=0;
    bool isX=false,isO=false;
    for(int i=0;i<4;i++)
    {
        X=0;O=0;
        for(int j=0;j<4;j++)
        {
            switch(game[j][i])
            {
                case 'O':
                    O++;
                    break;
                case 'T':
                    O++;
                    X++;
                    break;
                case 'X':
                    X++;
                    break;
            }
        }
        if(X==4)
            isX=true;
        if(O==4)
            isO=true;
    }
    if(isX && isO)
        return draw;
    if(isX)
        return Xwin;
    if(isO)
        return Owin;
    return notCompleted;
}
int checkD()
{
    int X=0,O=0,T=0;
    bool isX=false,isO=false;
    for(int i=0;i<4;i++)
    {
        switch(game[i][i])
        {
            case 'O':
                O++;
                break;
            case 'T':
                O++;
                X++;
                break;
            case 'X':
                X++;
                break;
        }
    }
    if(X==4)
        isX=true;
    if(O==4)
        isO=true;
    X=0;O=0;

    for(int i=0;i<4;i++)
    {
        switch(game[3-i][i])
        {
            case 'O':
                O++;
                break;
            case 'T':
                O++;
                X++;
                break;
            case 'X':
                X++;
                break;
        }
    }
    if(X==4)
        isX=true;
    if(O==4)
        isO=true;
    if(isX && isO)
        return draw;
    if(isX)
        return Xwin;
    if(isO)
        return Owin;
    return notCompleted;
}
string checkWin()
{
    empty=0;
    int v=checkV();
    int h=checkH();
    int d=checkD();
    //cout << v<<h<<d<< endl;
    if(v==draw || h==draw || d==draw)
        return "Draw";
    if((v==Xwin && h==Owin) || (h==Xwin && v==Owin) || (v==Xwin && d==Owin) || (d==Xwin && v==Owin) || (d==Xwin && h==Owin) || (h==Xwin && d==Owin))
        return "Draw";
    if((v==Xwin && h==notCompleted && d==notCompleted) || (v==notCompleted && h==Xwin && d==notCompleted) || (v==notCompleted && h==notCompleted && d==Xwin)|| (v==Xwin && h==Xwin && d==notCompleted)|| (v==Xwin && h==notCompleted && d==Xwin)|| (v==notCompleted && h==Xwin && d==Xwin)|| (v==Xwin && h==Xwin && d==Xwin))
        return "X won";
    if((v==Owin && h==notCompleted && d==notCompleted) || (v==notCompleted && h==Owin && d==notCompleted) || (v==notCompleted && h==notCompleted && d==Owin)|| (v==Owin && h==Owin && d==notCompleted)|| (v==Owin && h==notCompleted && d==Owin)|| (v==notCompleted && h==Owin && d==Owin)|| (v==Owin && h==Owin && d==Owin))
        return "O won";
    if(v==notCompleted && h==notCompleted && d==notCompleted && empty==0)
        return "Draw";
    else
        return "Game has not completed";
}
int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    string s;
    int T;
    cin >> T;
    for(int test=1;test<=T;test++)
    {
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin >> game[i][j];
                //cout << game[i][j];
            }
            //cout << endl;
        }
        cout << "Case #" << test <<": " << checkWin() << endl;
        //cout << endl << endl;
    }
    return 0;
}
