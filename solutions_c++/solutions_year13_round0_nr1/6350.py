#include <iostream>
#include <stdio.h>
using namespace std;
#include <fstream>
char now[5][5];
bool find(char x)
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            if(now[i][j]!=x&&now[i][j]!='T') break;
        if(j==4) return true;
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            if(now[j][i]!=x&&now[j][i]!='T') break;
        if(j==4) return true;
    }
    for(i=0;i<4;i++)
        if(now[i][i]!=x&&now[i][i]!='T') break;
    if(i==4) return true;
    for(i=0;i<4;i++)
        if(now[3-i][i]!=x&&now[3-i][i]!='T') break;
    if(i==4) return true;
    return false;
}
int main()
{
    int T,cnt = 1;
    ifstream fin("A-large.in");
    ofstream out("A-large.out");
    fin>>T;
    while(T--)
    {
        bool complete = true;
        for(int i=0;i<4;i++)
        {
            fin>>now[i];
            for(int j=0;j<4;j++)
                if(now[i][j]=='.') { complete = false; break; }
        }
        out<<"Case #"<<cnt++<<": ";
        if(find('X')) out<<"X won"<<endl;
        else if(find('O'))out<<"O won"<<endl;
        else if(complete) out<<"Draw"<<endl;
        else out<<"Game has not completed"<<endl;
    }
}
