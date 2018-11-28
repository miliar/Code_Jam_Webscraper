#include<iostream>
#include<string>
using namespace std;
int T;
string a[4];
void solve(int p)
{
    int i,j,l;
    l=0;
    if((a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')&&(a[2][2]=='X'||a[2][2]=='T')&&(a[3][3]=='X'||a[3][3]=='T'))
    {
        l=1;
        cout<<"Case #"<<p<<": X won";
    }
    if((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T')&&l!=1)
    {
        l=1;
        cout<<"Case #"<<p<<": X won";
    }
    if(!l)
    {
        for(i=0;i<4;i++)
        {
            if((a[i][0]=='X'||a[i][0]=='T')&&(a[i][1]=='X'||a[i][1]=='T')&&(a[i][2]=='X'||a[i][2]=='T')&&(a[i][3]=='X'||a[i][3]=='T')&&l!=1)
            {
                l=1;
                cout<<"Case #"<<p<<": X won";
            }
        }
        for(i=0;i<4;i++)
        {
            if((a[0][i]=='X'||a[0][i]=='T')&&(a[1][i]=='X'||a[1][i]=='T')&&(a[2][i]=='X'||a[2][i]=='T')&&(a[3][i]=='X'||a[3][i]=='T')&&l!=1)
            {
                l=1;
                cout<<"Case #"<<p<<": X won";
            }
        }
    }
    if(!l)
    {
        if((a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')&&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T'))
        {
            l=1;
            cout<<"Case #"<<p<<": O won";
        }
        if((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T')&&l!=1)
        {
            l=1;
            cout<<"Case #"<<p<<": O won";
        }
        for(i=0;i<4;i++)
        {
            if((a[i][0]=='O'||a[i][0]=='T')&&(a[i][1]=='O'||a[i][1]=='T')&&(a[i][2]=='O'||a[i][2]=='T')&&(a[i][3]=='O'||a[i][3]=='T')&&l!=1)
            {
                l=1;
                cout<<"Case #"<<p<<": O won";
            }
        }
        for(i=0;i<4;i++)
        {
            if((a[0][i]=='O'||a[0][i]=='T')&&(a[1][i]=='O'||a[1][i]=='T')&&(a[2][i]=='O'||a[2][i]=='T')&&(a[3][i]=='O'||a[3][i]=='T')&&l!=1)
            {
                l=1;
                cout<<"Case #"<<p<<": O won";
            }
        }
    }
    if(!l)
    {
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='.')
                {
                    l=1;
                    cout<<"Case #"<<p<<": Game has not completed";
                    break;
                }
            }
            if(l==1)break;
        }
        if(!l){cout<<"Case #"<<p<<": Draw";}
    }
    cout<<endl;
}
void read()
{
    int i,j,k;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>a[j];
        }
        solve(i);
    }
}
int main()
{
    read();
    return 0;
}