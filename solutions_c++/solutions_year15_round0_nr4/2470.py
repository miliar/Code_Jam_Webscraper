#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    freopen("c.in", "r",stdin);
    int t;
    cin >> t;
    for (unsigned int idx = 0; idx < t; idx++)
    {
        int x, r, c;
        cin >> x >> r >> c;
        cout << "Case #" << idx + 1 << ": ";
        if (x == 1)
            cout << "GABRIEL" << endl;
        else if (((r * c) % x != 0))
            cout << "RICHARD" << endl;
        else if ((x == 3) && (r * c == 3))
            cout << "RICHARD" << endl;
        else if ((x > c) && (x > r))
        {
            cout << "RICHARD" << endl;
        }
        else if ((x == 4) && ((r * c) == 8 || (r * c) == 4))
            cout << "RICHARD" << endl;
        else
            cout << "GABRIEL" << endl;
    }
    return 0;
}
