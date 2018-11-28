#include <fstream>
using namespace std;

int n, a[6][6], r1, r2, rs, rn, x[6],sol[6];

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");

    fin >> n;

    for (int i = 1; i <= n; ++i)
    {
        fin >> r1;
        rs = 0;
        for (int v = 1; v <= 4; ++v)
        {
            for (int b = 1; b <= 4; ++b)
            {
                fin >> a[v][b];
            }
        }
        for (int j = 1; j <= 4; ++j)
        {
            x[j] = a[r1][j];
        }
        fin >> r2;
        rn = 0;
          for (int v = 1; v <= 4; ++v)
        {
            for (int b = 1; b <= 4; ++b)
            {
                fin >> a[v][b];
            }
        }
        for (int j = 1; j <= 4; ++j)
        {
            for (int v = 1; v <= 4; ++v)
            {
                if (x[j] == a[r2][v])
                {
                    rs = x[j];
                    rn++;
                }
            }
        }
        if (rn == 0)
        {
            fout << "Case #" << i << ": Volunteer cheated!" << "\n";
        }
        else if (rn == 1)
        {
            fout << "Case #" << i << ": " << rs << "\n";
        }
        else
        {
            fout << "Case #" << i << ": Bad magician!" << "\n";
        }
    }

    return 0;
}