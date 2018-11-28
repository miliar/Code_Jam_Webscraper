#include<iostream>
#include<queue>
#include<string>
#include <cstdio>
#include<vector>
#include<cmath>
#include<ctime>
#include<memory.h>
#include<map>
#include <cmath>
#include<algorithm>
#include<set>
using namespace std;
#define y1 anaasfasf
bool good[105][105][4];
int n, m;
string s;
int t;
int arr[105][105];
void solve() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> s;
        for (int j = 0; j < m; ++j) {
            arr[i][j] = -1;
            if (s[j] == '>') t = 0;
            else if (s[j] == 'v') t = 1;
            else if (s[j] == '<') t = 2;
            else if (s[j] == '.') t = -1;
            else t = 3;
            arr[i][j] = t;
        }
    }
    memset(good, false, sizeof(good));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (arr[i][j] == -1) continue;
            int x = j + 1;
            while (x < m && arr[i][x] == -1) x++;
            good[i][j][0] = !(x == m);
            x = j - 1;
            while (x >= 0 && arr[i][x] < 0) x--;
            good[i][j][2] = !(x < 0);
            x = i + 1;
            while (x < n && arr[x][j] < 0) x++;
            good[i][j][1] = !(x == n);
            x = i - 1;
            while (x >= 0 && arr[x][j] < 0) x--;
            good[i][j][3] = !(x < 0);
        }
    }
    int ans = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            if (arr[i][j] == -1) continue;
            bool is = false;
            for (int q = 0; q < 4; ++q)
                is |= good[i][j][q];
            if (!is) {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
            if (!good[i][j][arr[i][j]])ans++;
        }
    cout << ans << endl;
}
int main() {
    #ifdef FurkoHome
        freopen("A-large.in","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    ios::sync_with_stdio(false);
    int T; cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    return 0;
}
