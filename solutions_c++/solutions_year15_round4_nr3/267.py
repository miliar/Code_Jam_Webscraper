#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
#define sz(A) (int((A).size()))

vector <string> read()
{
    string s;
    getline(cin, s);
    s += ' ';
    int pos = 0;
    vector <string> res;

    while (pos < sz(s))
    {
        int nxt = s.find(' ', pos);
        res.push_back(s.substr(pos, nxt - pos));
        pos = nxt + 1;
    }
    return res;
}

void brute(int pos, int cnt, map <string, int> &A, vector <vector <string> > &X, int &res)
{
    if (pos == sz(X))
        res = min(res, cnt);
    else
    {
        vector <int> vals(sz(X[pos]));

        for (int i = 0; i < sz(X[pos]); i++)
        {
            vals[i] = A[X[pos][i]];
        }

        for (int k = 1; k <= 2; k++)
        {
            int copy = cnt;

            for (int i = 0; i < sz(X[pos]); i++)
            {
                if (A[X[pos][i]] == 3 - k)
                {
                    A[X[pos][i]] = 3;
                    cnt++;
                }
                else if (A[X[pos][i]] == 0)
                    A[X[pos][i]] = k;
            }

            brute(pos + 1, cnt, A, X, res);

            for (int i = 0; i < sz(X[pos]); i++)
            {
                A[X[pos][i]] = vals[i];
            }
            cnt = copy;
        }
    }
}

int run()
{
    int n;
    cin >> n;
    map <string, int> A;
    string s;
    getline(cin, s);
    int cnt = 0, res = 0;

    for (int i = 1; i <= 2; i++)
    {
        vector <string> now = read();

        for (auto x: now)
        {
            if (A[x] == 3 - i)
            {
                A[x] = 3;
                cnt++;
            }
            else if (A[x] == 0)
                A[x] = i;
        }
        res += sz(now);
    }

    vector <vector <string> > X;

    for (int i = 0; i < n - 2; i++)
    {
        X.push_back(read());
        res += sz(X.back());
    }

    brute(0, cnt, A, X, res);
    return res;
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
