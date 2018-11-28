#include <fstream>
#include <iostream>
using namespace std;

int a[4][4], d[4][4], b[4], c[4], t, an1, an2;

ifstream f("A-small-attempt1.in");
ofstream g("out.txt");

int main()
{
    f >> t;
    for (int i = 0; i < t; i ++)
    {
        f >> an1;
        an1 --;
        for (int j = 0; j < 4; j ++)
            for (int k = 0; k < 4; k ++)
                f >> a[j][k];
        f >> an2;
        an2 --;
        for (int j = 0; j < 4; j ++)
            for (int k = 0; k < 4; k ++)
                f >> d[j][k];

        for (int j = 0; j < 4; j ++)
            c[j] = d[an2][j];
        for (int j = 0; j < 4; j ++)
            b[j] = a[an1][j];
        int found = 0;
        int elem = 0;
        for (int j = 0; j < 4; j ++)
            for (int k = 0; k < 4; k ++)
                if (b[j] == c[k])
                {
                    elem = b[j];
                    found ++;
                }
        if (!found)
            g << "Case #" << i + 1 << ": Volunteer cheated!";
        else
            if (found == 1)
                g << "Case #" << i + 1 << ": " << elem;
            else
                g << "Case #" << i + 1 << ": Bad magician!";
        g << endl;
    }
    return 0;
}
