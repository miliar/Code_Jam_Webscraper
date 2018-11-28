#include <iostream>
#include <functional>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool check(int a) {
    return a < 4 && a >= 0;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    for (int h = 1; h <= t; h++) {
        int n, m;
        bool yes = true;

        cin >> n >> m;
        vector<vector<int> > map(n, vector<int> (m));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> map[i][j];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                bool allgood = true;

                for (int k = 0; k < m; k++)
                    if (map[i][k] > map[i][j]) {
                        allgood = false;
                        break;
                    }

                if (allgood) continue;

                allgood = true;

                for (int k = 0; k < n; k++)
                    if (map[k][j] > map[i][j]) {
                        allgood = false;
                        break;
                    }

                if (!allgood) {
                    yes = false;
                    break;
                }
            }

            if (!yes) break;
        }

        cout << "Case #" << h << ": ";
        if (yes) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}

    
