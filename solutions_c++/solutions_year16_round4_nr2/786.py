#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
int n, m;
vector <double> p;
double best_ans;

double get(vector <int> &tmp)
{
    double dp[m + 1][m + 1];
    for (int i = 0; i <= m; ++i)
    {
        for (int j = 0; j <= m; ++j)
        {
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;
    for (int i = 1; i <= m; ++i)
    {
        dp[i][0] = dp[i - 1][0] * (1 - p[tmp[i - 1]]);
        for (int j = 1; j <= m; ++j)
            dp[i][j] = dp[i - 1][j] * (1 - p[tmp[i - 1]]) + dp[i - 1][j - 1] * p[tmp[i - 1]];
    }
    return dp[m][m / 2];
}

void gen(int cnt, vector <int> &tmp)
{
    if (tmp.size() == m)
    {
       best_ans = max(best_ans, get(tmp));
        return;
    }
    if (n - cnt == m - ((int)tmp.size()))
    {
        for (int i = cnt; i < n; ++i)
            tmp.push_back(i);
        best_ans = max(best_ans, get(tmp));
        for (int i = cnt; i < n; ++i)
            tmp.pop_back();
        return;
    }
    gen(cnt + 1, tmp);
    tmp.push_back(cnt);
    gen(cnt + 1, tmp);
    tmp.pop_back();
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cout.precision(20);
    int t;
    cin >> t;
    for (int _ = 1; _ <= t; ++_)
    {
        cout << "Case #" << _ << ": ";
        cin >> n >> m;
        p.clear();
        p.resize(n);
        for (int i = 0; i < n; ++i)
            cin >> p[i];

        best_ans = 0;
        vector <int> tmp;
        gen(0, tmp);
        cout << best_ans << endl;
    }
}
