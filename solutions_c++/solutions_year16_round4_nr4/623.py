/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 5;

int a[MAXN][MAXN];
int b[MAXN][MAXN];
int perm[MAXN];
int c[MAXN];

bool isValid(int N)
{
    for (int worker = 1; worker <= N; worker++)
    {
        for (int i = 1; i <= N; i++)
        {
            perm[i] = i;
        }

        do
        {
            for (int i = 1; i <= N; i++)
            {
                c[i] = 0;
            }

            int j = 1;
            for (int i = 1; i <= N; i++)
            {
                if (i != worker)
                {
                    if (b[i][ perm[j] ] == 1) c[ perm[j] ] = 1;
                    j++;
                }
            }

            bool canGo = false;
            for (int i = 1; i <= N; i++)
            {
                if (b[worker][i] == 1 && c[i] == 0) canGo = true;
            }

            if (!canGo)
            {
                //DEBUG(worker);
                return false;
            }
        }while(next_permutation(perm + 1, perm + N + 1));
    }

    return true;
}

int main()
{
    freopen("inputD.in", "r", stdin);
    freopen("outputD.out", "w", stdout);

    int _T;
    cin >> _T;

    for (int _t = 1; _t <= _T; _t++)
    {
        int N;
        cin >> N;

        int Z = 0;
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {
                char c;
                cin >> c;
                a[i][j] = c - '0';

                if (a[i][j] == 0)
                {
                    Z++;
                }
            }
        }

        int ans = Z;

        for (int mask = 0; mask < (1 << Z); mask++)
        {
            int cnt = 0;
            int curr = 0;
            for (int i = 1; i <= N; i++)
            {
                for (int j = 1; j <= N; j++)
                {
                    b[i][j] = a[i][j];
                    if (a[i][j] == 0 && ((1 << cnt) & mask) != 0)
                    {
                        b[i][j] = 1;
                        curr++;
                    }

                    if (a[i][j] == 0) cnt++;
                    //cout << b[i][j];
                }
                //cout << endl;
            }

            //if (isValid(N))
            //    cout << "Ok" << endl;
            //else
            //    cout << "Fail" << endl;

            if ((curr < ans) && isValid(N))
            {
                ans = curr;
            }
        }

        cout << "Case #" << _t << ": " << ans << endl;
    }

    return 0;
}
