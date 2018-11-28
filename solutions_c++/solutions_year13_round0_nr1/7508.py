#include <iostream>
#include <cstdio>
#include <string.h>
#include <fstream>
using namespace std;
char cc[4][4];

char judge(char tt)
{

    int ans;
    for (int i=0; i<4; i++)
    {
        ans=0;
        for (int j=0; j<4; j++)
        {
            if (cc[i][j]==tt || cc[i][j]=='T') ans++;
        }
        if (ans==4) return tt;
    }
    for (int i=0; i<4; i++)
    {
        ans=0;
        for (int j=0; j<4; j++)
        {
            if (cc[j][i]==tt || cc[j][i]=='T') ans++;
        }
        if (ans==4) return tt;
    }
    ans=0;
    for (int i=0; i<4; i++)
    {
        if (cc[i][i]==tt ||cc[i][i]=='T') ans++;
    }
    if (ans==4) return tt;

    ans=0;
    for (int i=0; i<4; i++)
    {
        if (cc[i][3-i]==tt || cc[i][3-i]=='T') ans++;
    }
    if (ans==4) return tt;
    return 'Q';
}

bool judged()
{
    for (int i=0;i<4;i++)
    {
        for (int j=0;j<4;j++)
        {
            if (cc[i][j]=='.') return false;
        }
    }
    return true;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    for (int nc=1; nc<=T; nc++)
    {
        for (int i=0; i<4; i++)
        {
            cin>>cc[i];
        }
        char w='Q';
        if (judge('X')=='X')
        {
            w='X';
            cout<<"Case #"<<nc<<": X won"<<endl;
            continue;
        }
        if (judge('O')=='O')
        {
            w='O';
            cout<<"Case #"<<nc<<": O won"<<endl;
            continue;
        }
        if (judged()) cout<<"Case #"<<nc<<": Draw"<<endl;
        else cout<<"Case #"<<nc<<": Game has not completed"<<endl;

    }
    return 0;
}
