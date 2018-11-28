#include <iostream>
#include <string>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("1.out");
int main()
{
    string s1 = "Bad magician!",
           s2 = "Volunteer cheated!";
    int t; fin >> t;
    for (int T=1; T<=t; T++)
    {
        int ans1, ans2;
        int a[5][5], b[5][5];
        fin >> ans1;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++) fin >> a[i][j];
        fin >> ans2;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++) fin >> b[i][j];
        int no, num = 0;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                if (a[ans1-1][i] == b[ans2-1][j]) { num ++; no = a[ans1-1][i]; }
        fout << "Case #" << T << ": ";
        if (num == 1) fout << no << endl;
        else if (num == 0) fout << s2 << endl;
        else fout << s1 << endl;
    }
    //system("pause");
    return 0;
}
