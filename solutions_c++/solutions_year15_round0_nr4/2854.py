//#define LARGE
#define SMALL

#include <iostream>
#include <algorithm>
using namespace std;

int t, T;
int X, R, C;

int main()
{
#if defined(LARGE)
    freopen("../D-large.in", "r", stdin);
    freopen("../D-large.out", "w", stdout);
#elif defined(SMALL)
    freopen("../D-small-attempt0.in", "r", stdin);
    freopen("../D-small.out", "w", stdout);
#else
    freopen("input.txt", "r", stdin);
#endif

    cin >> T;

    for (t = 1; t <= T; ++t)
    {
        cin >> X >> R >> C;
        if (X > 6 || R * C % X != 0) cout << "Case #" << t << ": RICHARD\n";
        else if (max(R, C) < X) cout << "Case #" << t << ": RICHARD\n";
        else if (min(R, C) == 1 && X > 2) cout << "Case #" << t << ": RICHARD\n";
        else if (min(R, C) == 2 && X > 3) cout << "Case #" << t << ": RICHARD\n";
        else if (min(R, C) == 3 && X > 5) cout << "Case #" << t << ": RICHARD\n";
        else cout << "Case #" << t << ": GABRIEL\n";
    }

    return 0;
}
