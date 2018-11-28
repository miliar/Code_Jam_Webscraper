#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <fstream>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <functional>

using namespace std;

int main(int argc, char ** argv)
{
    int T;
    while (cin >> T)
    {
        for (int cas = 1; cas <= T; cas++)
        {
            int N;
            double V, X;
            const double eps = 1e-9; 
            cin >> N >> V >> X;
            clog << N << ", " << V << ", " << X << endl;
            vector<pair<double, double> > a(N);
            double ans = 1e100, R = 0.0;
            for (auto & pr: a)
            {
                cin >> pr.first >> pr.second;
                //clog << "second = " << pr.second << ", X = " << X << endl;
                if ( abs(pr.second - X) < eps)
                {
                    R += pr.first;
                    ans = min(ans, V / R);
                }
            }

            double A, B, C, D, E, F;
            A = B = C = D = E = F = 0.0 ;
            bool up = false, dn = false;

            for (auto & i: a)
                if (i.second + eps < X)
                    A += i.first, C += i.first * i.second, up = true;
                else
                    B += i.first, D += i.first * i.second, dn = true;

            

            E = V, F = X * V;
            clog << A << ", " << B << ", " << E << endl;
            clog << C << ", " << D << ", " << F << endl;



            if (up && dn)
            {
                double y = (A * F - C * E) / (A * D - C * B);
                double x = (E - B * y)/ A;
                ans = min(ans, max(x, y));
            }


            if (ans + eps < 1e100)
                printf("Case #%d: %.6lf\n", cas, ans);
            else
                printf("Case #%d: IMPOSSIBLE\n", cas);
        }
    }
    return 0;
}
