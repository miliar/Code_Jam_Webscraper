#include <cassert>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int T = 1;
    int t;

    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;

        vector < vector <int> > grass(n, vector <int>(m));

        for (int i=0; i < n; ++i) {
            for (int j=0; j < m; ++j) {
                cin >> grass[i][j];
            }
        }

        bool valid = true;

        for (int i=0; i < n; ++i) {
            for (int j=0; j < m; ++j) {
                int biggestV = grass[i][j];
                int biggestH = grass[i][j];

                for (int k=0; k < n; ++k) {
                    biggestV = max(biggestV, grass[k][j]);
                }
                for (int k=0; k < m; ++k) {
                    biggestH = max(biggestH, grass[i][k]);
                }

                if (biggestH != grass[i][j] && biggestV != grass[i][j]) {
                    valid = false;
                    goto END;
                }
            }
        }

    END:
        cout << "Case #" << T++ << ": " << (valid ? "YES" : "NO") << endl;
    }

    return 0;
}
