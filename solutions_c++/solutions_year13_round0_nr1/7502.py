#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
using namespace std;
char s[5][5];
int judge()
{
    int f1=1,f2=1,f3=1,f4=1;
    int f=0;
    for(int i=0;i<4;i++)
    {
        int x1=1,x2=1,o1=1,o2=1;
        for(int j=0;j<4;j++)
        {
            if(s[i][j]!='X'&&s[i][j]!='T') x1=0;
            if(s[j][i]!='X'&&s[j][i]!='T') x2=0;
            if(s[i][j]!='O'&&s[i][j]!='T') o1=0;
            if(s[j][i]!='O'&&s[j][i]!='T') o2=0;
            if(s[i][j]=='.') f=1;
        }
        if(x1||x2) return 1;
        if(o1||o2) return 2;
        if(s[i][i]!='X'&&s[i][i]!='T') f1=0;
        if(s[i][3-i]!='X'&&s[i][3-i]!='T') f2=0;
        if(s[i][i]!='O'&&s[i][i]!='T') f3=0;
        if(s[i][3-i]!='O'&&s[i][3-i]!='T') f4=0;
    }
    if(f1||f2) return 1;
    if(f3||f4) return 2;
    return f==0?3:4;
}
int main()
{
    int T,kase=1;
    cin>>T;
    while(T--)
    {
        for(int i=0;i<4;i++)
        {
            cin>>s[i];
        }
        int tmp=judge();
        cout<<"Case #"<<kase++<<": ";
        if(tmp==1) cout<<"X won"<<endl;
        else if(tmp==2) cout<<"O won"<<endl;
        else if(tmp==3) cout<<"Draw"<<endl;
        else cout<<"Game has not completed"<<endl;
    }
    return 0;
}
