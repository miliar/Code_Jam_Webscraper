#include <cstdio>
#include <fstream>
#include <cmath>

using namespace std;

long long r,t;

int solve()
{
    long long x = 2*r+1;
    int n;
    for ( n = 1; n <= 707106785; n++)
    {
        long long s = (n+1)*(2*n+x);
        if(s > t)
        {
            break;
        }
    }
    return n;
    /*int k = 0;
    long long s = 0;
    while ( s <= t)
    {
        s += 2 * r + 1;
        r += 2;
        ++k;
    }

    if(s==t)
        return k;

    return k-1;*/
}

int main()
{
    ifstream f("in.txt");
    ofstream g("out.txt");

    int T, i;

    f >> T;
    for ( i = 1; i <= T; i++)
    {
        f >> r >> t;
        g << "Case #" << i << ": " << solve() << "\n";
    }
    f.close();
    g.close();

    return 0;
}
