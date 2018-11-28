#include <iostream>

using namespace std;

int main()
{
    int T, X, R, C;

    cin >> T;

    for (int c = 1; c <= T; c++)
    {

        cin >> X >> R >> C;

        cout << "Case #" << c << ": ";

        if (X == 1)
            cout << "GABRIEL" << endl;
        else if (X == 2)
        {
            if ((R*C)%2 == 0)
                cout << "GABRIEL" << endl;
            else
                cout << "RICHARD" << endl;
        }
        else if (X == 3)
        {
            if ((R*C) == 6 || R*C == 9 || R*C == 12)
                cout << "GABRIEL" << endl;
            else
                cout << "RICHARD" << endl;
        }
        else
        {
            if (R*C == 12 || R*C == 16)
                cout << "GABRIEL" << endl;
            else
                cout << "RICHARD" << endl;
        }
    }
    return 0;
}
