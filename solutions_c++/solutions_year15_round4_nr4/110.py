#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
#define sz(A) (int((A).size()))

bool check(const vector <vector <int> > &A)
{
    int r = sz(A), c = sz(A[0]);
    static const int dx[4] = {0, 1, 0, -1};
    static const int dy[4] = {1, 0, -1, 0};

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (A[i][j] == 0)
                continue;

            int now1 = 0, now2 = 0;

            for (int k = 0; k < 4; k++)
            {
                int ni = i + dx[k];
                int nj = (j + dy[k] + c) % c;

                if (ni >= 0 && ni < r)
                {
                    if (A[ni][nj] == A[i][j])
                    {
                        now1++;
                        now2++;
                    }
                    else if (A[ni][nj] == 0)
                        now2++;
                }
            }

            if (now1 > A[i][j] || now2 < A[i][j])
                return 0;
        }
    }
    return 1;
}

bool equal(const vector <vector <int> > &A, const vector <vector <int> > &B)
{
    int r = sz(A), c = sz(A[0]);

    for (int k = 0; k < c; k++)
    {
        bool now = 1;

        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                if (A[i][j] != B[i][(j + k) % c])
                    now = 0;

        if (now)
            return 1;
    }
    return 0;
}

void brute(vector <vector <int> > &A, int x, int y, vector <vector <vector <int> > > &res)
{
    int r = sz(A), c = sz(A[0]);

    if (x == r)
    {
        if (check(A))
        {
            bool flag = 1;

            for (auto &grid: res)
                if (equal(grid, A))
                    flag = 0;

            if (flag)
                res.push_back(A);
        }
    }
    else
    {
        for (int k = 1; k <= 4; k++)
        {
            A[x][y] = k;

            if (check(A))
            {
                brute(A, x + (y == c - 1), (y + 1) % c, res);
            }
            A[x][y] = 0;
        }
    }
}

int run()
{
    int r, c;
    cin >> r >> c;
    vector <vector <int> > A(r, vector <int>(c));
    vector <vector <vector <int> > > res;
    brute(A, 0, 0, res);
    return sz(res);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++)
    {
        cout << "Case #" << tst + 1 << ": " << run() << '\n';
    }

    return 0;
}
