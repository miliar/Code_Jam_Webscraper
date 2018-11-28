#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

char s[4][4];
int t;
int hasDot = 0;
ifstream fin("A-large.in");
ofstream fout("A-large.out");

int check()
{
    int result;
    //每行
    for(int i=0; i<4; i++)
    {
        int j=0;
        while(s[i][j] == 'T')
            j++;
        int first = s[i][j];

        for(j=0; j<4; j++)
        {
            if(s[i][j] != first && s[i][j]!='T') break;
        }
        if(j == 4)
            if(first == 'X') return 0;
            else if(first == 'O') return  1;
    }

    //每列
    for(int i=0; i<4; i++)
    {
        int j=0;
        while(s[j][i] == 'T')
            j++;
        int first = s[j][i];

        for(j=0; j<4; j++)
        {
            if(s[j][i] != first && s[j][i]!='T') break;
        }
        if(j == 4)
            if(first == 'X') return 0;
            else if(first == 'O')return 1;
    }

    //左对角线
    int i=0;
    while(s[i][i] == 'T') i++;
    int first = s[i][i];

    for(i=0; i<4; i++)
    {
        if(s[i][i] != first && s[i][i]!='T') break;
    }
    if(i == 4)
        if(first == 'X') return 0;
        else if(first == 'O')return 1;

    //右对角线
    i=0;
    while(s[i][3-i] == 'T') i++;
    first = s[i][3-i];

    for(i=0; i<4; i++)
    {
        if(s[i][3-i] != first && s[i][3-i]!='T') break;
    }
    if(i == 4)
        if(first == 'X') return 0;
        else if(first == 'O')return 1;

    //判断未完还是平局
    if(hasDot) return 3;
    else return 2;
}

int main()
{
    fin >> t;
    int round = 1;
    while(t--)
    {
        hasDot = 0;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                fin >> s[i][j];
                if(s[i][j]=='.') hasDot = 1;
            }

        int ch = check();
        fout << "Case #" << round++ << ": ";
        //fprintf(fout,"Case #%d: ",round); round++;
        if(ch == 0)
            fout << "X won\n";
        else if(ch == 1)
            fout << "O won\n";
        else if(ch == 2)
            fout << "Draw\n";
        else
            fout << "Game has not completed\n";

    }

    return 0;
}
