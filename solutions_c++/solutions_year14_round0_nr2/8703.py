#include <fstream>
#include <cmath>
#include <iomanip>

using namespace std;
const double err = 1e-9;

int main()
{
    ifstream f ("B1.in");
    ofstream g ("B1.out");

    int T;
    double C, F, X;
    f >> T;
    g.precision(16);
    for(int t = 1; t <= T; t++)
    {
        f >> C >> F >> X;
        double s = (X/C - 1 - 2.0/F);
        if (s < err)
        {
            g << "Case #" << t << ": ";
            g << (X / 2.0) << endl;
        }
        else
        {
            int n = floor(s + 0.5);
            if (F*n + 2.0 + err < (X/C - 1) * F) n++;
            double ans = X/(2.0 + n*F);
            for (int k = 0; k < n; k++)
                ans += C/(2.0 + k*F);
            g << "Case #" << t << ": ";
            g << ans << endl;
        }
    }

    return 0;
}
