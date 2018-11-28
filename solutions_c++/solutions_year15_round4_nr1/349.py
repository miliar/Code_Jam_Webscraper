#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
#define sz(A) (int((A).size()))

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++)
    {
        int r, c;
        cin >> r >> c;
        vector <string> A(r);

        for (int i = 0; i < r; i++)
        {
            cin >> A[i];
        }
        int res = 0;

        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                bool flag = 1;

                for (int k = 0; k < i; k++)
                    if (A[k][j] != '.')
                        flag = 0;
                
                for (int k = i + 1; k < r; k++)
                    if (A[k][j] != '.')
                        flag = 0;
                
                for (int k = 0; k < j; k++)
                    if (A[i][k] != '.')
                        flag = 0;

                for (int k = j + 1; k < c; k++)
                    if (A[i][k] != '.')
                        flag = 0;

                if (flag && A[i][j] != '.')
                {
                    res = -1;
                }
            }
        }

        if (res == -1)
        {
            cout << "Case #" << tst + 1 << ": IMPOSSIBLE" << '\n';
            continue;
        }

        for (int i = 0; i < r; i++)
        {
            int j = 0;

            while (j < c && A[i][j] == '.')
                j++;

            if (j < c && A[i][j] == '<')
                res++;

            j = c - 1;

            while (j >= 0 && A[i][j] == '.')
                j--;

            if (j >= 0 && A[i][j] == '>')
                res++;
        }

        for (int j = 0; j < c; j++)
        {
            int i = 0;

            while (i < r && A[i][j] == '.')
                i++;

            if (i < r && A[i][j] == '^')
                res++;

            i = r - 1;

            while (i >= 0 && A[i][j] == '.')
                i--;

            if (i >= 0 && A[i][j] == 'v')
                res++;
        }
        cout << "Case #" << tst + 1 << ": " << res << '\n';
    }

    return 0;
}
