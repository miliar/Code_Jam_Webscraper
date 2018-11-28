#include <fstream>
#include <cstring>
#include <iomanip>

#define maxn 110

using namespace std;

ifstream fin("test.in");
ofstream fout("test.out");

int n;
double r[10], c[10],X,V;

double solve()
{
    fin >> n >> V >> X;

    for (int i = 1; i <= n; ++i)
    {
        fin >> r[i] >> c[i];
    }

    if (n == 1)
    {
        if (X != c[1])
            return -1;
        else return V/r[1];
    }
    else
    {
        if (c[1] == c[2] && X != c[1])
            return -1;
        if (c[1] == c[2])
        {
           double R = r[1] + r[2];
            return V/R;
        }
        double v1 = (X*V - V*c[2])/(c[1] - c[2]);
        double v2 = V - v1;

        if (v1 < 0 || v2 < 0)
            return -1;
        return max(v1/r[1],v2/r[2]);
    }
}

void reset()
{
}

int main()
{
    int test;

    fin >> test;

    for (int k = 1; k <= test; ++k)
    {
        reset();
        double answer = solve();
        fout << "Case #" << k << ": ";
        if (answer == -1)
            fout << "IMPOSSIBLE";
        else fout << fixed << setprecision(7) << answer;
        fout << "\n";
    }
}
