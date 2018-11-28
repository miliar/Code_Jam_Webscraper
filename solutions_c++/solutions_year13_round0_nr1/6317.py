#include <iostream>
using namespace std;

int main () {
    int t;
    char board[4][4];
    cin>>t;
    for (int z=1;z<=t;z++)
    {
        bool notfull=false;
        bool xwin = false;
        bool owin = false;
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
                cin>>board[i][j];
                if (board[i][j]=='.')
                {
                   notfull=true;
                }
            }
        }
        int x = 0;
        int o = 0;
        for (int i=0;i<4 && !xwin && !owin;i++)
        {
            for (int j=0;j<4;j++)
            {
                if (board[i][j]=='X')
                {
                    x++;
                }
                else if (board[i][j]=='O')
                {
                     o++;
                }
                else if (board[i][j]=='T')
                {
                     x++;
                     o++;
                }
                //cout<<x<<" "<<o<<endl;
            }
            if (x==4) { xwin = true; }
            if (o==4) { owin = true; }
            x=0;
            o=0;
        }
        for (int j=0;j<4 && !xwin && !owin;j++)
        {
            for (int i=0;i<4;i++)
            {
                if (board[i][j]=='X')
                {
                    x++;
                }
                else if (board[i][j]=='O')
                {
                     o++;
                }
                else if (board[i][j]=='T')
                {
                     x++;
                     o++;
                }
                //cout<<x<<" "<<o<<endl;
            }
            if (x==4) { xwin = true; }
            if (o==4) { owin = true; }
            x=0;
            o=0;
        }
        for (int i=0;i<4 && !xwin && !owin;i++)
        {
            if (board[i][i]=='X')
            {
                x++;
            }
            else if (board[i][i]=='O')
            {
                 o++;
            }
            else if (board[i][i]=='T')
            {
                 x++;
                 o++;
            }
            //cout<<x<<" "<<o<<endl;
        }
        if (x==4) { xwin = true; }
        if (o==4) { owin = true; }
        x=0;
        o=0;
        int j=0;
        for (int i=3;i>=0 && !xwin && !owin;i--)
        {
            if (board[j][i]=='X')
            {
                x++;
            }
            else if (board[j][i]=='O')
            {
                 o++;
            }
            else if (board[j][i]=='T')
            {
                 x++;
                 o++;
            }
            j++;
        }
        if (x==4) { xwin = true; }
        if (o==4) { owin = true; }
        x=0;
        o=0;
        if (xwin)
        {
            cout<<"Case #"<<z<<": X won"<<endl;
        }
        else if (owin)
        {
            cout<<"Case #"<<z<<": O won"<<endl;
        }
        else if (!xwin && !owin && !notfull)
        {
            cout<<"Case #"<<z<<": Draw"<<endl;
        }
        else if (!xwin && !owin && notfull)
        {
            cout<<"Case #"<<z<<": Game has not completed"<<endl;
        }
    }
}
