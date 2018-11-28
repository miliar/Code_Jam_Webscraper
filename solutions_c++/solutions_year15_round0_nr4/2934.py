#include <iostream>
#include <cstdio>

using namespace std;

int n, x, r, c;

int main()
{
    freopen("D-small-attempt3.in", "r", stdin);
    freopen("d.txt", "w", stdout);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x >> r >> c;
        cout << "Case #" << i + 1 << ": ";
        if (x == 1) cout << "GABRIEL" << endl;
        else if (x == 2) {
            if (r % 2 == 0 || c % 2 == 0) cout << "GABRIEL" << endl;
            else cout << "RICHARD" << endl;
        }
        else if (x == 3) {
            if ((r % 3 == 0 || c % 3 == 0) && c != 1 && r != 1) cout << "GABRIEL" << endl;
            else cout << "RICHARD" << endl;
        }
        else if (x == 4) {
            if (c >= 3 && r >= 3 && (c != 3 || r != 3)) cout << "GABRIEL" << endl;
            else cout << "RICHARD" << endl;
        }
    }
    return 0;
}
