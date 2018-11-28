#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

int getScore(vector< vector< bool > > &a)
{
    int ans = 0;
    int n = a.size();
    int m = a[0].size();

    for(int i = 0; i < n; ++i)
    {
        for(int j = 1; j < m; ++j)
        {
            if(a[i][j] && a[i][j-1])
            {
                ++ans;
            }
        }
    }

    for(int j = 0; j < m; ++j)
    {
        for(int i = 1; i < n; ++i)
        {
            if(a[i][j] && a[i-1][j])
            {
                ++ans;
            }
        }
    }

    return ans;
}

int brute(int r, int c, int num)
{
    if(num == 0)
        return 0;

    vector<bool> x;

    for(int i = 0; i < num; ++i)
        x.push_back(true);

    int rc = r * c;
    while(x.size() < rc)
        x.push_back(false);

    x.push_back(false);
    reverse(x.begin(), x.end());

    int best = rc*5;

    vector< vector< bool > > a(r, vector<bool>(c) );

    while(!x[0])
    {
//        for(int i = 0; i < x.size(); ++i)
//            cout << x[i];
//        cout << endl;

        int i = 0;
        int j = 0;
        for(int k = 1; k < x.size(); ++k)
        {
            a[i][j] = x[k];
            ++i;
            if(i >= r)
            {
                i -= r;
                ++j;
            }
        }

        best = min(best, getScore(a));

        next_permutation(x.begin(), x.end());
    }

    return best;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);


    int TTT;
    cin >> TTT;
    for(int T = 1; T <= TTT; ++T)
    {
        int r, c, n;
        cin >> r >> c >> n;

        int ans = brute(r, c, n);

        cout << "Case #" << T << ": " << ans << endl;
    }

    return 0;
}
