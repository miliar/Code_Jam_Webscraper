#include <iostream>

using namespace std;

int main()
{
    int t;
    char a[5][5];
    int rx[5], ro[5], cx[5], co[5], do1, do2, dx1, dx2, count;
    bool xwin, owin;
    cin>>t;
    for (int ll=1;ll<=t;++ll)
    {
        //init
        do1=0; do2=0; dx1=0; dx2=0;
        count=0;
        xwin=0; owin=0;
        for (int i=1;i<=4;++i)
        {
            rx[i]=0;
            ro[i]=0;
            cx[i]=0;
            co[i]=0;
        }
        //row & col
        for (int i=1;i<=4;++i)
        for (int j=1;j<=4;++j)
        {
            cin>>a[i][j];
            if (a[i][j]=='X')
            {
                ++cx[i];
                ++rx[j];
                ++count;
            }
            else if (a[i][j]=='O')
            {
                ++co[i];
                ++ro[j];
                ++count;
            }
            else if (a[i][j]=='T')
            {
                ++cx[i];
                ++rx[j];
                ++co[i];
                ++ro[j];
                ++count;
            }
        }
        //diagonal
        for (int i=1;i<=4;++i)
        {
            if (a[i][i]=='X') ++dx1;
            else if (a[i][i]=='O') ++do1;
            else if (a[i][i]=='T')
            {
                ++dx1;
                ++do1;
            }

            if (a[i][5-i]=='X') ++dx2;
            else if (a[i][5-i]=='O') ++do2;
            else if (a[i][5-i]=='T')
            {
                ++dx2;
                ++do2;
            }
        }
        //check
        for (int i=1;i<=4;++i)
        {
            if (rx[i]==4 || cx[i]==4) xwin=1;
            if (ro[i]==4 || co[i]==4) owin=1;
        }
        if (dx1==4 || dx2==4) xwin=1;
        if (do1==4 || do2==4) owin=1;
        //output
        if (xwin) cout<<"Case #"<<ll<<": X won"<<endl;
        else if (owin) cout<<"Case #"<<ll<<": O won"<<endl;
        else if (count==16) cout<<"Case #"<<ll<<": Draw"<<endl;
        else cout<<"Case #"<<ll<<": Game has not completed"<<endl;
    }
}
