#include <bits/stdc++.h>

using namespace std;

int p[10005][20][20], n, m, res[10005], ans[10005], T;
string s;

int CalC(char i)
{
    if (i == 'i') return 2;
    if (i == 'j') return 3;
    if (i == 'k') return 4;
}

int Mul(int i, int j)
{
    int sign = i*j  < 0 ? -1 : 1;
    if (i < 0) i = -i;
    if (j < 0) j = -j;
    if (i == 1 || j == 1) return sign*i*j;
    if (i == j) return -sign;
    if (i == 2) return j == 3 ? sign*4 : -3*sign;
    if (i == 3) return j == 2 ? -sign*4 : 2*sign;
    if (i == 4) return j == 2 ? sign*3 : -2*sign;
}

int main()
{
    freopen("in.in", "r", stdin);
    freopen("ou.out", "w", stdout);

    cin >> T;
    for (int itest = 0; itest < T; itest++)
    {
        cin >> n >> m;
        cin >> s;
        memset(p, 0, sizeof(p));
        memset(ans, 0, sizeof(ans));
        memset(res, 0, sizeof(res));
        ans[m*n] = 1;
        for (int i = 0; i < n*m; i++) res[i] = i > 0 ? Mul(res[i - 1], CalC(s[i % n])) : CalC(s[i % n]);
        for (int i = m*n - 1; i >= 0; i--) ans[i] = Mul(CalC(s[i % n]), ans[i + 1]);

        for (int i = m*n - 2; i >= 0; i--)
        {
            p[i][res[i] + 10][ans[i + 1] + 10] = 1;
            for (int j = -4; j <= 4; j++)
                for (int k = -4; k <= 4; k++)
                    if (i != 0 && j != 0) p[i][j + 10][k + 10] |= p[i + 1][j + 10][k + 10];
        }

        int j = 0;
        for (int i = 0; i < m*n - 2 && j == 0; i++)
            if (res[i] == 2 && p[i + 1][Mul(2, 3) + 10][4 + 10] == 1) j = 1;


        cout << "Case #" << itest + 1 << ": ";
        if (j == 1) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}
