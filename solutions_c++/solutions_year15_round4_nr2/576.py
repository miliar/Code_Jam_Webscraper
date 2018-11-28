#include <bits/stdc++.h>

using namespace std;

bool eq(double a, double b)
{
    return a + 1e-10 > b && a - 1e-10 < b;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int TESTS;
    cin >> TESTS;
    for (int TEST = 1; TEST <= TESTS; ++TEST)
    {
        cout << "Case #" << TEST << ": ";
        int n;
        double v, x;
        cin >> n >> v >> x;
        vector<pair<double, double>> V(n);
        for (auto & x : V)
            cin >> x.first >> x.second;
        if (n == 1)
        {
            if (!eq(x, V[0].second))
                cout << "IMPOSSIBLE\n";
            else
                cout << setprecision(20) << v / V[0].first << '\n';
        }
        else if ((V[0].second - 1e-10 > x && V[1].second - 1e-10 > x) || (V[0].second + 1e-10 < x && V[1].second + 1e-10 < x))
            cout << "IMPOSSIBLE\n";
        else if (eq(x, V[0].second))
        {
            if (eq(x, V[1].second))
                cout << setprecision(20) << v / (V[0].first + V[1].first) << '\n';
            else
                cout << setprecision(20) << v / V[0].first << '\n';
        }
        else if (eq(x, V[1].second))
            cout << setprecision(20) << v / V[1].first << '\n';
        else
        {
            double q = 1. / (abs(V[0].second - x) / abs(V[1].second - x));
            double a = v * q / (q + 1), b = v / (q + 1);
            cout << setprecision(20) << max(a / V[0].first, b / V[1].first) << '\n';
        }
    }
    return 0;
}
