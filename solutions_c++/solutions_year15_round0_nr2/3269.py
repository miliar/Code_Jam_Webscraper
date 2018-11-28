#include <iostream>
#include <fstream>

using namespace std;

const long long INFLL = 4000000000000000000LL;
const int NMax = 1024;
int a[NMax];

int main()
{
    ifstream f ("input.txt");
    ofstream g ("output.txt");
    int nr_tests; f >> nr_tests;
    for (int test = 1; test <= nr_tests; ++ test)
    {
        int N; f >> N;
        for (int i = 1; i <= N; ++ i)
            f >> a[i];
        int maxim = 0;
        for (int i = 1; i <= N; ++ i)
            maxim = max(maxim, a[i]);
        long long timpmin = INFLL;
        for (int p = maxim; p >= 1; -- p)
        {
            long long timp = 0LL;
            for (int i = 1; i <= N; ++ i)
            {
                if (a[i] % p == 0)
                    timp += (a[i] / p - 1);
                else
                    timp += a[i] / p;
            }
            timp += p;
            timpmin = min(timpmin, timp);
        }
        g << "Case #" << test << ": " << timpmin << "\n";
    }
    f.close();
    g.close();
    return 0;
}
