#include <iostream>
#include <cstdio>
#include <cmath>
#include <memory.h>

using namespace std;

const double e = 1e-9;

double m_max(double a, double b)
{
    if (a < b) return b;
    else return a;
}

double mod(double x)
{
    if (x < 0) return -x;
    else return x;
}

double r[105], c[105];
double v, x;

int main() {
    cout.setf(ios::fixed);
    cout.precision(7);
    freopen("B-small-attempt0(1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int n;
        cin >> n;
        cin >> v >> x;
        for (int i = 0; i < n; ++i)
            cin >> r[i] >> c[i];
        double t_min = 10000000;
        for (int i = 0; i < n; ++i)
            for (int j = i; j < n; ++j)
            {
                if (i == j)
                {
                    if (mod(c[i] - x) > e)
                        continue;
                    if (mod(c[i] - x) < e)
                        if (t_min > v / r[i])
                            t_min = v / r[i];
                    continue;
                }
                if(c[i] > x && c[j] > x)
                    continue;
                if (c[i] < x && c[j] < x)
                    continue;
                if (mod(c[i] - c[j]) < e && mod(x - c[i]) > e)
                    continue;
                if (mod(c[i] - c[j]) < e && mod(x - c[i]) < e)
                {
                    double v2 = v / (1 + r[i] / r[j]);
                    double v1 = v - v2;
                    if (t_min > v1 / r[i])
                        t_min = v1 / r[i];
                } else {
                    double v1 = v * x - v * c[j];
                    v1 = v1 / (c[i] - c[j]);
                    if (m_max(v1 / r[i],(v - v1) / r[j]) < t_min)
                        t_min = m_max(v1 / r[i],(v - v1) / r[j]);
                }
            }
        if (t_min == 10000000) {
            cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << "\n";
            continue;
        }
        cout << "Case #" << t + 1 << ": " << t_min << "\n";
    }
    return 0;
}
