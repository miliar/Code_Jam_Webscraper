#include <iostream>

using namespace std;

void Solve()
{
     double r, t;
     cin >> r >> t;
     int i = 1;
     double a1 = 2 * r + 1, d = 4;
     while (((2 * a1 + (i - 1) * d) / 2) * i <= t)
     {
         ++i;
     }
     cout << i - 1 << endl;
}

int main()
{
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": ";
        Solve();
    }
    return 0;
}
