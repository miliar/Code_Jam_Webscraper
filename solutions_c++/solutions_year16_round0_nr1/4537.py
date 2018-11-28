#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fi ("A-large.in");
    ofstream fo ("output_large.txt");
    int t;
    fi >> t;
    for (int o = 1; o <= t; ++o)
    {
        long int n, i = 0;
        fi >> n;
        if (n == 0)
        {
            fo << "Case #" << o << ": INSOMNIA" << endl;
            continue;
        }
        int a[10] = {0};
        while (!(a[0]*a[1]*a[2]*a[3]*a[4]*a[5]*a[6]*a[7]*a[8]*a[9]))
        {
            long int x = ++i * n;
            while (x)
            {
                a[x % 10] += 1;
                x = x / 10;
            }
        }
        fo << "Case #" << o << ": " << i * n << endl;
    }
}
