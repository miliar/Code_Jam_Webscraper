#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        return 1;
    }
    char name[256];
    strcpy(name, argv[1]);

    ifstream fin(name);
    name[strlen(name)-2] = 0;
    strcat(name, "out");
    ofstream fout(name);

    if (!fin.is_open() || !fout.is_open())
    {
        return 1;
    }

    int t, t1 = 0;

    fin >> t;

    while (t1++ < t)
    {
        unsigned int a, b, k;
        fin >> a >> b >> k;
        unsigned int c = 0;
        for (unsigned int i = 0; i < a; i++)
        {
            for (unsigned int j = 0; j < b; j++)
            {
                if ((i & j) < k)
                {
                    c++;
                }
            }
        }

        fout << "Case #" << t1 << ": ";
        fout << c << endl;

    }

    return 0;
}