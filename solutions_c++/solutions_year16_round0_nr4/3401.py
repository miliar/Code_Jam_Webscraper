#include <iostream>
#include <fstream>

using namespace std;

long long int power(int x, int p)
{
    if (p == 1) return x;
    if (p == 0) return 1;
    long long int y = power (x, p / 2);
    if (p % 2) return (x * y * y);
    else return (y * y);
}

int main()
{
    ifstream fi ("D-small-attempt0.in");
    ofstream fo ("output_small.txt");
    int t;
    fi >> t;
    for (int o = 1; o <= t; ++o)
    {
        int k, c, s;
        fi >> k >> c >> s;
        fo << "Case #" << o << ": ";
        long long int x = power(k, c - 1);
        for (int i = 1; i <= k; ++i)
        {
            fo << x * (i - 1) + 1 << " ";
        }
        fo << endl;
    }
}
