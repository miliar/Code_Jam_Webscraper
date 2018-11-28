#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <utility>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>

using namespace std;

typedef long long LL;
template<class T> inline T Abs(const T& x) { return x < 0 ? -x : x; }
template<class T> inline T Sqr(const T& x) { return x * x; }


const char* letters = ">v<^";
const int dy[4] = {0, +1, 0, -1};
const int dx[4] = {+1, 0, -1, 0};


typedef vector<string> TField;

int GetDirection(char c) {
    int d = 0;
    while (letters[d] != c) {
        ++d;
    }
    return d;
}


void Solution() {
    int n, m;
    cin >> n >> m;
    TField f;
    f.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> f[i];
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (f[i][j] != '.') {
                int d = GetDirection(f[i][j]);
                int bad = true;
                for (int k = 1; ; ++k) {
                    int y = i + dy[d] * k;
                    int x = j + dx[d] * k;
                    if (y < 0 || y >= n || x < 0 || x >= m) {
                        break;
                    } else if (f[y][x] != '.') {
                        bad = false;
                        break;
                    }
                }
                if (bad) {
                    bool possible = false;
                    for (int d = 0; d < 4; ++d) {
                        bool good = false;
                        for (int k = 1; ; ++k) {
                            int y = i + dy[d] * k;
                            int x = j + dx[d] * k;
                            if (y < 0 || y >= n || x < 0 || x >= m) {
                                break;
                            }
                            if (f[y][x] != '.') {
                                good = true;
                                break;
                            }
                        }
                        if (good) {
                            possible = true;
                            break;
                        }
                    }
                    if (possible) {
                        ++ans;
                    } else {
                        cout << "IMPOSSIBLE" << endl;
                        return;
                    }
                }
            }
        }
    }
    cout << ans << endl;
}


int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        float startTime = clock() / CLOCKS_PER_SEC;
        cout << "Case #" << i + 1 << ": ";
        Solution();
        float endTime = clock() / CLOCKS_PER_SEC;
        cerr << "Test #" << i + 1 << ": elapsed time is " << endTime - startTime;
        cerr << endl;
    }

    return 0;
}


