#include <bits/stdc++.h>

using namespace std;

int update(int b, int c[])
{
    while (b)
    {
        c[b % 10] = 1;
        b /= 10;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("P.out", "w", stdout);

    int t, a[10], casee = 0, n;

    cin >> t;

    while (t--)
    {
        casee++;

        cin >> n;

        int p=1, m=n;

        for (int i=0; i<=9; i++) a[i]=0;

        if (n == 0)
        {
            cout << "Case #" << casee << ": INSOMNIA" << endl;
            p=0;
        }

        while (p)
        {
            update(n, a);

            int k=0;

            for (int i=0; i<=9; i++) if (a[i] == 0) k++;

            if (k == 0)
            {
                p = 0;
                cout << "Case #" << casee << ": " << n << endl;
            }

            n += m;
        }
    }
}
