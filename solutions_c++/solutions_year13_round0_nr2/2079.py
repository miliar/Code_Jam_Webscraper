#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int k = 1; k <= T; ++k) {
        int n,m;
        cin >> n >> m;
        int minn[110];
        int minm[110];
        memset(minn, 0, sizeof(minn));
        memset(minm, 0, sizeof(minm));
        int board[110][110];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> board[i][j];
                minn[i] = max(minn[i], board[i][j]);
                minm[j] = max(minm[j], board[i][j]);
            }
        }
        bool ok = 1;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (board[i][j] < minn[i] && board[i][j] < minm[j])
                    ok = 0;
        cout << "Case #" << k << ": " << (ok ? "YES" : "NO") << endl;
    }
}
