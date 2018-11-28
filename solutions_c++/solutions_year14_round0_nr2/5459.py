#include <iostream>
#include <iomanip>

using namespace std;

int T;
double C, F, X;

void Solve(int t)
{
    double maxK = (X * F - 2 * C) / (C * F);
    int k = maxK < 0 ? 0 : static_cast<int>(maxK);
    double time = 0;
    for (int i = 0; i < k; ++i)
    {
        time += C / (2 + i * F);
    }
    time += X / (2 + k * F);
    cout << "Case #" << t << ": " << time << endl;
}

int main()
{
    cout << fixed << setprecision(7);
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> C >> F >> X;
        Solve(t);
    }
}