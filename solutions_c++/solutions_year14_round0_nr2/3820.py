#include <bits/stdc++.h>


std::ifstream in("B-large.in");
std::ofstream out("output.txt");
const int M = 100001;


int main()
{
    int T;
    in >> T;
    for (int t = 1; t <= T; ++t)
    {
        out << "Case #" << t << ": ";
        double c, f, x;
        in >> c >> f >> x;
        double d[M] = {};
        double dm = x / 2.0;
        int j;
        for (j = 1; j < M; ++j)
        {
            double k = 2.0 + (j - 1) * f;
            d[j] = d[j - 1] + c / k;
            if (d[j] > dm) break;
        }
        double ans = 1e15;
        for (int i = 0; i < j; ++i)
        {
            double ps = 2.0 + f * i;
            double cost = d[i] + x / ps;
            ans = std::min(ans, cost);
        }
        out << std::fixed << std::setprecision(7) << ans << std::endl;
    }
}
