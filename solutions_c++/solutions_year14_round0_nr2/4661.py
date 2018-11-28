#include <fstream>
#include <iomanip>
using namespace std;

#define in "test.in"
#define out "test.out"
#define FOR(i, T) for(int i = 1; i <= T; ++i)

ifstream f(in);
ofstream g(out);

int T;
double C, F, X, ans, scnds;

int main()
{
    f >> T;

    FOR(i, T)   {
        ans = 0, scnds = 2;
        f >> C >> F >> X;

        while(X / scnds + ans > ans + X / (scnds + F) + C / scnds)  {
            ans += C / scnds;
            scnds += F;
        }

        g << fixed << setprecision(7) << "Case #" << i << ": " << ans + X / scnds;
        if(i < T)   g << '\n';
    }

    g.close();
    return 0;
}
