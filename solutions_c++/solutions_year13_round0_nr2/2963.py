#include <string>
#include <iostream>
using namespace std;

#define for_(i, a, b) for (int i = a; i < b; ++i)


int main(void) {
    int t;
    cin >> t;

    for_(T, 1, t+1) {
        int n, m;
        cin >> n >> m;

        int lawn[n][m];
        for_(i, 0, n) for_(j, 0, m) cin >> lawn[i][j];

        bool error = false;
        for_(i, 0, n) for_(j, 0, m) {
            bool ok_vert = true;
            for_(i2, 0, n) if (lawn[i2][j] > lawn[i][j]) {
                ok_vert = false;
                break;
            }

            bool ok_hor = true;
            for_(j2, 0, m) if (lawn[i][j2] > lawn[i][j]) {
                ok_hor = false;
                break;
            }

            if (!ok_vert && !ok_hor) {
                error = true;
                goto out;
            }
        }

        out:
        cout << "Case #" << T << ": " << (error ? "NO" : "YES") << endl;
    }
}
