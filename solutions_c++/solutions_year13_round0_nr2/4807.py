#include <iostream>

using namespace std;

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    int n, m;
    int map[105][105];
    int map2[105][105];
    int rowmax;
    int colmax;
    const int maxv = 200;
    bool result;

    for (coden = 1; coden <= t; coden++)
    {
        cin >> n >> m;
        for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
            map2[i][j] = maxv;
        }
        for (int i = 0; i < n; i++) {
            rowmax = 0;
            for (int j = 0; j < m; j++) {
                if (map[i][j] > rowmax) {
                    rowmax = map[i][j];
                }
            }
            // mow the row
            for (int j = 0; j < m; j++) {
                if (map2[i][j] > rowmax) {
                    map2[i][j] = rowmax;
                }
            }
        }
        for (int j = 0; j < m; j++) {
            colmax = 0;
            for (int i = 0; i < n; i++) {
                if (map[i][j] > colmax) {
                    colmax = map[i][j];
                }
            }
            // mow the column
            for (int i = 0; i < n; i++) {
                if (map2[i][j] > colmax) {
                    map2[i][j] = colmax;
                }
            }
        }

        // check the ans
        result = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] != map2[i][j]) {
                    result = false;
                    break;
                }
            }
            if (!result) break;
        }
        // output result
        cout << "Case #" << coden << ": " << (result ? "YES" : "NO") << endl;
    }
    return 0;
}

