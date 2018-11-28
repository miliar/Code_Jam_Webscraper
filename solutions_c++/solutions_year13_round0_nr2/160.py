#include <iostream>
#include <vector>
using namespace std;

int main() {

    int tc;
    cin >> tc;

    for (int t = 1; t <= tc; t++) {
        int m, n;
        cin >> m >> n;
        vector<vector<int> > pattern(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cin >> pattern[i][j];
            }
        }

        vector<int> horizontalCuts(m, 0);
        vector<int> verticalCuts(n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pattern[i][j] > horizontalCuts[i]) {
                    horizontalCuts[i] = pattern[i][j];
                }
                if (pattern[i][j] > verticalCuts[j]) {
                    verticalCuts[j] = pattern[i][j];
                }
            }
        }

        vector<vector<int> > grass(m, vector<int>(n, 100));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grass[i][j] > horizontalCuts[i]) {
                    grass[i][j] = horizontalCuts[i];
                }
                if (grass[i][j] > verticalCuts[j]) {
                    grass[i][j] = verticalCuts[j];
                }
            }
        }

        string ans = (grass == pattern) ? "YES" : "NO";
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

