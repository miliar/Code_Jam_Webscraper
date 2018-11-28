#include <fstream>
#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
ifstream f("B-small-attempt0.in");
ofstream g("sol.out");

int t, a, b, k;

int main()
{
    f >> t;
    for (int i = 1; i <= t; i ++)
    {
        g << "Case #"<< i << ": ";
        f >> a >> b >> k;
        int numar = 0;
        for (int j = 0; j < a; j ++)
            for (int l = 0; l < b; l ++)
            {
                int local = j & l;
                if (local < k)
                {
                    numar ++;
                }
            }
        g << numar << endl;
    }
    return 0;
}
