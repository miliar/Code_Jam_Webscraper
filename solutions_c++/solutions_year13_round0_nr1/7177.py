#include <fstream>
#include <iostream>
#include <string>

using namespace std;

    ifstream in ("1.in");
    ofstream out ("output");

string doProblem(string s[4])
{
    bool xFlag=0;
    bool oFlag=0;
    bool isEmptyCells=0;

    for (int i=0; i< 4; ++i)
    {
        bool xFlazhok=1;
        bool oFlazhok=1;
        for (int j=0; j<4; ++j)
        {
            isEmptyCells |= s[i][j]=='.';
            xFlazhok&=(s[i][j]=='T'|s[i][j]=='X');

            oFlazhok&=(s[i][j]=='T'|s[i][j]=='O');

        }
        xFlag|=xFlazhok;
        oFlag|=oFlazhok;

    }
    for (int i=0; i< 4; ++i)
    {
        bool xFlazhok=true;
        bool oFlazhok=true;
        for (int j=0; j<4; ++j)
        {
            xFlazhok&=(s[j][i]=='T'|s[j][i]=='X');
            oFlazhok&=(s[j][i]=='T'|s[j][i]=='O');
        }
        xFlag|=xFlazhok;
        oFlag|=oFlazhok;
    }
    bool xFlazhok=true;
        bool oFlazhok=true;

    for (int i=0; i< 4; ++i)
    {
        xFlazhok&=(s[i][i]=='T'|s[i][i]=='X');
        oFlazhok&=(s[i][i]=='T'|s[i][i]=='O');

    }
        xFlag|=xFlazhok;
        oFlag|=oFlazhok;
    xFlazhok=true;
    oFlazhok=true;

    for (int i=0; i< 4; ++i)
    {
        xFlazhok&=(s[i][3-i]=='T'|s[i][3-i]=='X');
        oFlazhok&=(s[i][3-i]=='T'|s[i][3-i]=='O');

    }
    xFlag|=xFlazhok;
        oFlag|=oFlazhok;

    if (oFlag)
    {return " O won";}
    else if (xFlag)
        {return " X won";}

    else if (isEmptyCells)
        {return " Game has not completed";}

    else
        return " Draw";
}

int main()
{
    int n;
    in >> n;
    string s[4];
    string bin;
    for (int i=0; i<n; ++i)
    {
        for (int i=0; i<4; ++i)
            in >> s[i];
        //in >> bin;
        //out << s[0] <<"\n"<< s[1] <<"\n"<< s[2] <<"\n"<< s[3] <<"\n";
        out << "Case #" << i+1 << ":"<< doProblem(s) << endl;
    }

    return 0;
}
