#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

int main()
{
    //int a;
    ofstream out;
    int i,j;
    int bla;
    int testcases;
    int test;
    int bla2;
    cin >> testcases;
    string a[testcases][4];
    out.open ("output.txt");
    for (test=0; test<testcases; test++) {
    for (j=0; j<4; j++)
    {
        cin >> a[test][j];
    }
    // WON X
    // 1st case
    for (i=0; i<4; i++)
    {
        if ( (a[test][i][0]=='X' || a[test][i][0]=='T') && (a[test][i][1]=='X' || a[test][i][1]=='T') && (a[test][i][2]=='X' || a[test][i][2]=='T') && (a[test][i][3]=='X' || a[test][i][3]=='T'))
        {
            a[test][0] = "X won";
        }
        if ( (a[test][0][i]=='X' || a[test][0][i]=='T') && (a[test][1][i]=='X' || a[test][1][i]=='T') && (a[test][2][i]=='X' || a[test][2][i]=='T') && (a[test][3][i]=='X' || a[test][3][i]=='T'))
        {
            a[test][0] = "X won";
        }
    }
    //diagonalebi 1
    if ( (a[test][0][0]=='X' || a[test][0][0]=='T') && (a[test][1][1]=='X' || a[test][1][1]=='T') && (a[test][2][2]=='X' || a[test][2][2]=='T') && (a[test][3][3]=='X' || a[test][3][3]=='T'))
        {
            a[test][0] = "X won";
        }
    //dia[test]gona[test]lebi 2
    if ( (a[test][0][3]=='X' || a[test][0][3]=='T') && (a[test][1][2]=='X' || a[test][1][2]=='T') && (a[test][2][1]=='X' || a[test][2][1]=='T') && (a[test][3][0]=='X' || a[test][3][0]=='T'))
        {
            a[test][0] = "X won";
        }

    // WON O
        for (i=0; i<4; i++)
    {
        if ( (a[test][i][0]=='O' || a[test][i][0]=='T') && (a[test][i][1]=='O' || a[test][i][1]=='T') && (a[test][i][2]=='O' || a[test][i][2]=='T') && (a[test][i][3]=='O' || a[test][i][3]=='T'))
        {
            a[test][0] = "O won";
        }
        if ( (a[test][0][i]=='O' || a[test][0][i]=='T') && (a[test][1][i]=='O' || a[test][1][i]=='T') && (a[test][2][i]=='O' || a[test][2][i]=='T') && (a[test][3][i]=='O' || a[test][3][i]=='T'))
        {
            a[test][0] = "O won";
        }
    }
    //diagonalebi 1
    if ( (a[test][0][0]=='O' || a[test][0][0]=='T') && (a[test][1][1]=='O' || a[test][1][1]=='T') && (a[test][2][2]=='O' || a[test][2][2]=='T') && (a[test][3][3]=='O' || a[test][3][3]=='T'))
        {
            a[test][0] = "O won";
        }
    //diagonalebi 2
    if ( (a[test][0][3]=='O' || a[test][0][3]=='T') && (a[test][1][2]=='O' || a[test][1][2]=='T') && (a[test][2][1]=='O' || a[test][2][1]=='T') && (a[test][3][0]=='O' || a[test][3][0]=='T'))
        {
            a[test][0] = "O won";
        }

    bla = 0;
    for (i=0; i<4; i++) {
        for (j=0; j<4; j++){
            if (a[test][j][i]=='.') (bla++);
        }
    }
    //game not completed
    if ( (a[test][0]!="O won" && a[test][0]!="X won") && bla>0 )
    {
        a[test][0] = "Game has not completed";
    }

    if ( (a[test][0]!="O won" && a[test][0]!="X won") && bla==0 )
    {
        a[test][0] = "Draw";
    }

    }

    cout << "\n";

    for (i=0; i<testcases; i++) {
    cout << "Case #" << i+1 << ": " << a[i][0] << endl;
    out << "Case #" << i+1 << ": " << a[i][0] << endl;
    }

    cout << "\n";
    out << "\n";

    out.close();

 return 0;

}
