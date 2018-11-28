#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int x, r, c;
        cin >> x >> r >> c;

        if (r * c % x)
        {
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
            continue;
        }

        if (r < x && c < x)
        {
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
            continue;
        }

        if (x >= 7)
        {
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
            continue;
        }

        if (x > 2 && (r <= x / 2 || c <= x / 2))
        {
            cout << "Case #" << i + 1 << ": RICHARD" << endl;
            continue;
        }

        cout << "Case #" << i + 1 << ": GABRIEL" << endl;
    }
    return 0;
}

