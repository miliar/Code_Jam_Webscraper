#include <fstream>

using namespace std;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");

    int t;
    fin >> t;
    for (int i = 0; i < t; i++)
    {
        int x, r, c;
        fin >> x >> r >> c;

        if ((r * c) % x != 0 || max(r, c) < x)
        {
            fout << "Case #" << (i + 1) << ": RICHARD" << endl;
            continue;
        }

        if (x <= 2)
        {
            fout << "Case #" << (i + 1) << ": GABRIEL" << endl;
            continue;
        }

        if (min(r, c) < 3)
        {
            if (min(r, c) == 1)
            {
                fout << "Case #" << (i + 1) << ": RICHARD" << endl;
                continue;
            }
            else
            {
                if (x == 3)
                {
                    fout << "Case #" << (i + 1) << ": GABRIEL" << endl;
                    continue;
                }
                else
                {
                    fout << "Case #" << (i + 1) << ": RICHARD" << endl;
                    continue;
                }
            }
        }
        else
        {
            fout << "Case #" << (i + 1) << ": GABRIEL" << endl;
            continue;
        }
    }
    return 0;
}
