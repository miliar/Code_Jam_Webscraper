#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int X, R, C;
        cin >> X >> R >> C;

        bool y = false;

        if ((R < X && C < X) || (R >= X && C < X-1) || (R < X-1 && C >= X))
            y = true;
        else if (((R * C) % X != 0 || R < ceil(X/2.f) || C < ceil(X/2.f)))
            y = true;
        else
            y = false;

        if (y)
            cout << "Case #" << t+1 << ": " << "RICHARD" << endl;
        else
            cout << "Case #" << t+1 << ": " << "GABRIEL" << endl;
    }
}
