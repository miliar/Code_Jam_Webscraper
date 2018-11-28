#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    map<char, int> tp;
    int dx[] = {0, 1, 0, -1};
    int dy[] = {1, 0, -1, 0};
    tp['>'] = 0;
    tp['v'] = 1;
    tp['<'] = 2;
    tp['^'] = 3;
    for(int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        int n, m;
        cin >> n >> m;
        string a[n];
        for(int i = 0; i < n; i++)
            cin >> a[i];
        int ans = 0;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
            {
                if(a[i][j] == '.')
                    continue;
                int t = tp[a[i][j]];
                for(int x = i + dx[t], y = j + dy[t]; x < n && x >= 0 && y < m && y >= 0; x += dx[t], y += dy[t])
                    if(a[x][y] != '.')
                        goto NXT;
                ans++;
                for(int t = 0; t < 4; t++)
                for(int x = i + dx[t], y = j + dy[t]; x < n && x >= 0 && y < m && y >= 0; x += dx[t], y += dy[t])
                    if(a[x][y] != '.')
                        goto NXT;
                cout << "IMPOSSIBLE\n";
                goto nxt;
                NXT:;
            }
        cout << ans << "\n";
        nxt:;
    }
}
