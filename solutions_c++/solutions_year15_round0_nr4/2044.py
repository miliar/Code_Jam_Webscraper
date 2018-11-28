#include <iostream>
#include <vector>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o = 0; o < t; o++) {
        int x, r, c;
        cin >> x >> r >> c;

        if (x == 1) {
            cout << "Case #" << o + 1 << ": " << "GABRIEL" << endl;
        } else if (x == 2) {
            if (r * c % 2 == 0) {
                cout << "Case #" << o + 1 << ": " << "GABRIEL" << endl;
            } else {
                cout << "Case #" << o + 1 << ": " << "RICHARD" << endl;
            }
        } else if (x == 3) {
            if (r > c) {
                swap(r, c);
            }
            if (r == 2 && c == 3) {
                cout << "Case #" << o + 1 << ": " << "GABRIEL" << endl;
            } else if (r == 3 && c == 3) {
                cout << "Case #" << o + 1 << ": " << "GABRIEL" << endl;
            } else if (r == 3 && c == 4) {
                cout << "Case #" << o + 1 << ": " << "GABRIEL" << endl;
            } else {
                cout << "Case #" << o + 1 << ": " << "RICHARD" << endl;
            }
        } else {
            if (r > c) {
                swap(r, c);
            }
            if (r == 3 && c == 4) {
                cout << "Case #" << o + 1 << ": " << "GABRIEL" << endl;
            } else if (r == 4 && c == 4) {
                cout << "Case #" << o + 1 << ": " << "GABRIEL" << endl;
            } else {
                cout << "Case #" << o + 1 << ": " << "RICHARD" << endl;
            }
        }

    }
    return 0;
}
