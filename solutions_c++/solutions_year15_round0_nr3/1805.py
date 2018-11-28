#include <iostream>

using namespace std;

int m[8][8] = {
    {0, 1, 2, 3},
    {1, 4, 3, 6},
    {2, 7, 4, 1},
    {3, 2, 5, 4}};

int x[8][8];
int y[8][8];

char s[1 << 17];
int a[1 << 17];
int b[1 << 17];

int main()
{
    for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
        {
            m[i + 4][j + 4] = m[i][j];
            m[i + 4][j] = m[i][j + 4] = m[i][j] ^ 4;
        }

    for (int i=0; i<8; i++)
        for (int j=0; j<8; j++)
        {
            x[i][m[i][j]] = j;
            y[j][m[i][j]] = i;
        }

    int t;
    cin >> t;


    for (int tt=1; tt<=t; tt++)
    {
        int n;
        long long k;
        cin >> n >> k;

        if (k > 11)
            k = k % 4 + 8;

        cerr << n * k << endl;

        cin >> s;
        for (int i=n; i < k*n; i++)
            s[i] = s[i - n];

        n *= k;

        for (int i=0; i<n; i++)
            s[i] = s[i] == '1' ? 0 : s[i] == 'i' ? 1 : s[i] == 'j' ? 2 : s[i] == 'k' ? 3 : 4;

        a[0] = 0;
        for (int i=0; i<n; i++)
            a[i + 1] = m[a[i]][s[i]];

        b[n] = 0;
        for (int i=n-1; i>=0; i--)
            b[i] = m[s[i]][b[i + 1]];

        bool ok = false;

        for (int i=1; i<n && !ok; i++)
            if (a[i] == 1)
                for (int j=i+1; j<n; j++)
                    ok |= b[j] == 3 && x[a[i]][a[j]] == 2;

        cout << "Case #" << tt << ": " << (ok ? "YES" : "NO") << endl;
    }

    return 0;
}
