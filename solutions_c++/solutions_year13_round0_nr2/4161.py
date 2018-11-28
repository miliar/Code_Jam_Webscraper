#include "iostream"
#include "string.h"

using namespace std;

int main(int argc, char const *argv[])
{
    int t;
    int n, m;
    cin >> t;
    for (int s = 0; s < t; ++s) {
        cin >> n >> m;
        // cout << n <  < " " << m << endl;
        int lawn[n][m];
        int imax[n], imin[n], jmax[m], jmin[m];
        int max = -1, min = 101;
        memset_pattern4(imax, &max, n * sizeof(int));
        memset_pattern4(jmax, &max, m * sizeof(int));
        memset_pattern4(imin, &min, n * sizeof(int));
        memset_pattern4(jmin, &min, m * sizeof(int));
        // for (int i = 0; i < n; ++i) {
        //     cout << imax[i] << "-" << imin[i] << " ";
        // }
        // cout << endl;
        // for (int i = 0; i < m; ++i) {
        //     cout << jmax[i] << "-" << jmin[i] << " ";
        // }
        // cout << endl;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> lawn[i][j];
                // cout << lawn[i][j] << " ";
                if (lawn[i][j] > imax[i]) { imax[i] = lawn[i][j]; }
                if (lawn[i][j] > jmax[j]) { jmax[j] = lawn[i][j]; }
                if (lawn[i][j] < imin[i]) { imin[i] = lawn[i][j]; }
                if (lawn[i][j] < jmin[j]) { jmin[j] = lawn[i][j]; }
            }
        }
        bool possible = true;
        // for (int i = 0; i < n; ++i) {
        //     cout << imax[i] << "-" << imin[i] << " ";
        // }
        // cout << endl;
        // for (int i = 0; i < m; ++i) {
        //     cout << jmax[i] << "-" << jmin[i] << " ";
        // }
        // cout << endl;
        for (int i = 0; i < n && possible; ++i) {
            for (int j = 0; j < m; ++j) {
                // if (lawn[i][j] > imin[i] && lawn[i][j] > jmin[j]) {
                //     possible = false;
                //     break;
                // }
                if (lawn[i][j] < imax[i] && lawn[i][j] < jmax[j]) {
                    possible = false;
                    break;
                }
            }
        }
        printf("Case #%d: %s\n", s + 1, (possible) ? "YES" : "NO");
    }
    cout << endl;
    return 0;
}