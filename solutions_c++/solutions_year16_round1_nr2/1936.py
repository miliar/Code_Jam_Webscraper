#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fi ("B-large.in");
    ofstream fo ("output_large.txt");
    int t;
    fi >> t;
    for (int o = 1; o <= t; ++o)
    {
        int n;
        fi >> n;
        int a[2501] = {0}, var;
        for (int i = 0; i < 2*n - 1; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                fi >> var;
                a[var] += 1;
            }
        }
        fo << "Case #" << o << ": ";
        for (int i = 0; i < 2501; ++i)
        {
            if (a[i] % 2) fo << i << " ";
        }
        fo << endl;
    }
}
