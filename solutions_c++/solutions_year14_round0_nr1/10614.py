#include <fstream>
#include <iostream>
using namespace std;
int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int N;
    in >> N;
    for (int i = 0; i < N; i++)
    {
        int m1[4][4], m2[4][4], s1, s2;
        in >> s1;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                in >> m1[j][k];
        in >> s2;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                in >> m2[j][k];
        int res = 0;
        int nres = 0;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                if (m1[s1-1][j] == m2[s2-1][k])
                {
                    res = m1[s1-1][j];
                    nres++;
                }
        out << "Case #" << i+1 <<": ";
        if (nres == 0)
            out << "Volunteer cheated!" << endl;
        else if (nres > 1)
            out << "Bad magician!" << endl;
        else out << res << endl;
    }
}
