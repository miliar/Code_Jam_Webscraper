#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

const int NMax = 1024;
char a[NMax];

int main()
{
    ifstream f("input.txt");
    ofstream g("output.txt");
    int nr_tests; f >> nr_tests;
    for (int test = 1; test <= nr_tests; ++ test)
    {
        int N; f >> N;
        f >> a;
        int added = 0, now = 0;
        for (int i = 0; i <= N; ++ i)
        {
            if (now >= i)
            {
                now += a[i] - '0';
            }
            else
            {
                if (a[i] == '0')
                    continue;
                int nr = i - now;
                added += nr;
                now += nr;
                now += a[i] - '0';
            }
        }
        g << "Case #" << test << ": " << added << "\n";
    }
    f.close();
    g.close();
    return 0;
}
