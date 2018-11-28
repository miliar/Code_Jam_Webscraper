#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream fout("output.out");
    ifstream fin("input.in");
    int test, a, b, k, c, res;
    fin >> test;

    for(int i = 0; i < test; ++i)
    {
        res = 0;
        fout << "Case #" << i + 1 << ": ";

        fin >> a >> b >> k;

        for(int j = 0; j < a; ++j)
        {
            for(int l = 0; l < b; ++l)
            {
                c = j & l;
                if(c < k)
                    res++;
            }
        }
        fout << res << endl;
    }

    return 0;
}
