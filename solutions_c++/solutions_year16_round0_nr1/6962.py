#include <iostream>
#include <fstream>
using namespace std;
long long n, baz;
int T, viz;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");
    fin >> T;
    for(int t = 1; t <= T; ++t)
    {
        fin >> n;
        if(n == 0)
        {
            fout << "Case #" << t << ": " << "INSOMNIA" << "\n";
            continue;
        }
        viz = 0;
        baz = n;
        while(viz != (1 << 10) - 1)
        {
            long long x = n;
            while(x > 0)
            {
                int cif = x % 10;
                viz = (viz | (1 << cif));
                x /= 10LL;
            }
            if(viz != (1 << 10) - 1)
                n += baz;
        }
        fout << "Case #" << t << ": " << n << "\n";
    }
    fin.close();
    fout.close();
    return 0;
}

