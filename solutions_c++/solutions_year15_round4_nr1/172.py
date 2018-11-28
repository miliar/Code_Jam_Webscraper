#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        int r, c;
        cin >> r >> c;
        vector<string> a(r);
        for (int i = 0; i < r; ++i)
            cin >> a[i];
        bool fail = false;
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j) {
                if (a[i][j] != '.') {
                    bool empty = true;
                    for (int ii = 0; ii < r; ++ii)
                        for (int jj = 0; jj < c; ++jj) {
                            if ((i == ii || j == jj) && !(i == ii && j == jj) && a[ii][jj] != '.')
                                empty = false;
                        }
                    if (empty)
                        fail = true;
                }
            }
        int ans = 0;
        if (!fail) {
            for (int i = 0; i < r; ++i)
                for (int j = 0; j < c; ++j) {
                    bool empty = (a[i][j] != '.');
                    if (a[i][j] == '^') {
                        for (int k = i - 1; k >= 0; --k)
                            if (a[k][j] != '.')
                                empty = false;
                    } else if (a[i][j] == '>') {
                        for (int k = j + 1; k < c; ++k)
                            if (a[i][k] != '.')
                                empty = false;
                    } else if (a[i][j] == 'v') {
                        for (int k = i + 1; k < r; ++k)
                            if (a[k][j] != '.')
                                empty = false;
                    } else if (a[i][j] == '<') {
                        for (int k = j - 1; k >= 0; --k)
                            if (a[i][k] != '.')
                                empty = false;
                    }
                    if (empty)
                        ++ans;
                }
        }
        cout << "Case #" << cs << ": ";
        if (fail)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
    return 0;
}
