#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;


bool isok(const vector< vector<int> >& grass, int r, int c)
{
    // either all of the row or all of the col need to be less or equal to spot (r,c)

    // see if all the row is less or equal
    bool ok = true;
    for (size_t j = 0; j < grass[r].size(); j++)
        if (grass[r][j] > grass[r][c])
            ok = false;
    if (ok)
        return true;

    // see if all the col is less or equal
    ok = true;
    for (size_t i = 0; i < grass.size(); i++)
        if (grass[i][c] > grass[r][c])
            ok = false;
    if (ok)
        return true;

    return false;
}


void solve()
{
    int n, m;
    cin >> n >> m;
    vector< vector<int> > grass(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> grass[i][j];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (! isok(grass, i, j))
            {
                cout << "NO" << endl;
                return;
            }

    cout << "YES" << endl;
}


int main()
{
    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        cout << "Case #" << caseNum << ": ";
        solve();
    }

    return 0;
}
