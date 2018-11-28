#include <iostream>
#include <stdio.h>
#include <cstring>
#include <fstream>
using namespace std;
int a[4][4];
int b[4][4];
int t[17];
int c1,c2;
fstream fin,fout;
int n;
int main()
{
    fin.open("A-small-attempt0.in",ios::in);
    fout.open("ans0.out",ios::out);
    fin >> n;
    for (int l = 0; l < n; l++)
    {
        for (int i = 1; i <= 16; i++) t[i] = 0;
        fin >> c1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                fin >> a[i][j];
        for (int i = 0; i < 4; i++) t[a[c1-1][i]]++;
        fin >> c2;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                fin >> b[i][j];
        for (int i = 0; i < 4; i++) t[b[c2-1][i]]++;

        int check1 = 0, check2 = 0;
        for (int i = 1; i <= 16; i++)
            if (t[i] == 2)
                if (check1 == 0 && check2 == 0) {check1 = 1; check2 = i;}
                else check2 = -1;
        if (check2 > 0)
            fout << "case #" << l+1 << ": " << check2 << endl;
        else if (check2 < 0)
            fout << "case #" << l+1 << ": Bad magician!" << endl;
        else
            fout << "case #" << l+1 << ": Volunteer cheated!" << endl;
    }
    fout.close();
}
