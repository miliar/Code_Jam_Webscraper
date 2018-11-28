#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int TESTS;
    cin >> TESTS;
    for (int TEST = 1; TEST <= TESTS; ++TEST)
    {
        cout << "Case #" << TEST << ": ";
        int h, w;
        cin >> h >> w;
        vector<vector<char>> V(h, vector<char>(w));
        for (auto & x : V)
            for (auto & y : x)
                cin >> y;
        reverse(V.begin(), V.end());
        vector<vector<int>> Ans(h, vector<int>(w, 0));
        for (int i = 0; i < h; i++)
            for (int j = 0; j < w; j++)
            {
                int x = j, y = i, lastx = -1, lasty = i, steps = w * h + 5;
                char direct = '.';
                while (steps && x >= 0 && x < w && y >= 0 && y < h)
                {
                    if (V[y][x] != '.')
                    {
                        direct = V[y][x];
                        lastx = x;
                        lasty = y;
                    }
                    switch (V[y][x])
                    {
                    case 'v':
                        y--;
                        break;
                    case '<':
                        x--;
                        break;
                    case '^':
                        y++;
                        break;
                    case '>':
                        x++;
                        break;
                    default:
                        switch (direct)
                        {
                        case 'v':
                            y--;
                            break;
                        case '<':
                            x--;
                            break;
                        case '^':
                            y++;
                            break;
                        case '>':
                            x++;
                            break;
                        default:
                            break;
                        }
                        break;
                    }
                    steps--;
                }
                if (steps)
                {
                    Ans[lasty][lastx]++;
                }
            }
        int ans = 0;
        for (int i = 0; i < h && ans != -1; i++)
            for (int j = 0; j < w && ans != -1; j++)
                if (Ans[i][j])
                {
                    bool ok = false;
                    for (int k = i + 1; k < h; k++)
                        ok |= (V[k][j] != '.');
                    for (int k = i - 1; k >= 0; k--)
                        ok |= (V[k][j] != '.');
                    for (int k = j + 1; k < w; k++)
                        ok |= (V[i][k] != '.');
                    for (int k = j - 1; k >= 0; k--)
                        ok |= (V[i][k] != '.');
                    if (!ok)
                        ans = -1;
                    else
                        ++ans;
                }
        if (ans == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << '\n';
    }
    return 0;
}
