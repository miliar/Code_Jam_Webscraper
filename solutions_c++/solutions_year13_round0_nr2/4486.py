// qualB.cpp
//
// on each cut, it cuts to the max height

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void solve(int tcase)
{
    cout << "Case #" << tcase << ": ";

    int N, M; cin >> N >> M;
    int lawn[105][105];
    for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
        cin >> lawn[i][j];

    int height[105][105];
    for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
        height[i][j] = 100;

    bool update = true;
    while (update) {
        update = false;
        // cut row
        for (int i = 0; i < N; ++i) {
            int mx = 0;
            for (int j = 0; j < M; ++j) mx = max(lawn[i][j], mx);
            for (int j = 0; j < M; ++j) {
                if (height[i][j] > mx) {
                    height[i][j] = mx;
                    update = true;
                }
            }
        }
        // cut col
        for (int j = 0; j < M; ++j) {
            int mx = 0;
            for (int i = 0; i < N; ++i) mx = max(lawn[i][j], mx);
            for (int i = 0; i < N; ++i) {
                if (height[i][j] > mx) {
                    height[i][j] = mx;
                    update = true;
                }
            }
        }
    }
    bool ans = true;
    for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
        if (height[i][j] != lawn[i][j]) {
            ans = false;
        }
    if (ans) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; ++t)
        solve(t);
}

