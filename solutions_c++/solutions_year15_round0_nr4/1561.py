#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int n;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int X, C, R;

        cin >> X >> C >> R;

        if (X >= 7)
        {
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
            continue;
        }

        if (X == 4 && (C == 2 || R == 2))
        {
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
            continue;
        }

        if (C < X && R < X)
        {
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
            continue;
        }

        if (C * R % X != 0)
        {
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
            continue;
        }

        int aux = X / 2 + X % 2;
        if (C < aux || R < aux)
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
        else cout << "Case #" << i + 1 << ": GABRIEL" << endl;
    }
}
