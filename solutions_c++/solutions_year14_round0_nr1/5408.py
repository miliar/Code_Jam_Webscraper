#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

ifstream lire("input.in", ios::in);
ofstream ecrire("output.txt", ios::out);

int main()
{
    int T;
    lire >> T;
    for (int k = 1; k <= T; k++)
    {
        int r, b = 0, s;
        int l[4];
        lire >> r;
        for (int i = 1; i <= 4; i++)
            for (int j = 0; j < 4; j++)
            {
                int u;
                lire >> u;
                if (i == r)
                    l[j] = u;
            }
        lire >> r;
        for (int i = 1; i <= 4; i++)
            for (int j = 0; j < 4; j++)
            {
                int u;
                lire >> u;
                if (i == r && (l[0] == u or l[1] == u or l[2] == u or l[3] == u))
                {
                    b++;
                    s = u;
                }
            }
        ecrire << "Case #" << k << ": ";
        if (b == 0)
            ecrire << "Volunteer cheated!" << endl;
        else if (b > 1)
            ecrire << "Bad magician!" << endl;
        else
            ecrire << s << endl;
    }
    return 0;
}
