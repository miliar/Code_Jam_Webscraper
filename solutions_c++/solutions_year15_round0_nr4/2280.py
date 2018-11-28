#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <string>

using namespace std;


int main()
{
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w",stdout);
    int T;
    cin >> T;
    for (int z = 0; z < T; ++z)
    {
        string S = "GABRIEL";
        int X, R, C;
        cin >> X >> R >> C;
        if ((X > R && X > C) || (X >= 3 && (C == 1 || R == 1)) || (((R * C) / X) * X != R * C))
        {
            S = "RICHARD";
        }

        int b = max(R,C);
        int a = min(R,C);
        R = b;
        C = a;
        if (R == 4 && C == 2 && X == 4)
        {
            S = "RICHARD";
        }
        cout << "Case #" << z + 1 << ": " << S << endl;
    }
    return 0;
}
