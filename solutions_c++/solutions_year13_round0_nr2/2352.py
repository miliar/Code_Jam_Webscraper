#include <iostream>
#include <vector>

using namespace std;

bool solve()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int> > h(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> h[i][j];
        }
    }

    for (int i = 100; i > 0; --i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                if (h[j][k] == i) {
                    bool possible = true;
                    for (int x = 0; x < n; ++x) {
                        if (h[x][k] > i) {
                            possible = false;
                            break;
                        }
                    }
                    if (possible) continue;
                    possible = true;
                    for (int y = 0; y < m; ++y) {
                        if (h[j][y] > i) {
                            possible = false;
                            break;
                        }
                    }
                    if (!possible) return false;
                }
            }
        }
    }
    return true;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << (solve() ? "YES" : "NO") << endl;
    }
    return 0;
}
