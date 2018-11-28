#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
#define sz(A) (int((A).size()))

int main()
{
    ios::sync_with_stdio(0);

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++)
    {
        int r, c, n;
        cin >> r >> c >> n;
        int res = r * c * 8;

        for (int i = 0; i < (1 << (r * c)); i++)
        {
            vector <vector <int> > table(r, vector <int>(c));

            for (int j = 0; j < r * c; j++)
                if ((i >> j) & 1)
                    table[j / c][j % c] = 1;
            int now = 0;

            for (int x1 = 0; x1 < r; x1++)
                for (int y1 = 0; y1 < c; y1++)
                    now += table[x1][y1];
            
            if (now != n)
                continue;
            now = 0;
            
            for (int x1 = 0; x1 < r; x1++)
                for (int y1 = 0; y1 < c; y1++)
                    for (int x2 = 0; x2 < r; x2++)
                        for (int y2 = 0; y2 < c; y2++)
                            if (abs(x1 - x2) + abs(y1 - y2) == 1 && table[x1][y1] == 1 && table[x2][y2] == 1)
                                now++;
            res = min(res, now);
        }
        cout << "Case #" << tst + 1 << ": " << res / 2 << '\n';
    }
    return 0;
}
