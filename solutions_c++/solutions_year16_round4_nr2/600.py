#include <iostream>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cassert>
#include <vector>
using namespace std;

double p[201];
double dp[201][201];
int n, m;
double calc(const vector<double> &a)
{
    memset(dp , 0 , sizeof dp);
    dp[0][0] = 1;
    for (int i = 1 ; i <= m ; ++i)
        for (int j = 0 ; j <= m ; ++j)
            dp[i][j] = (j ? a[i - 1] * dp[i - 1][j - 1] : 0)+ (1.0 - a[i - 1]) * dp[i - 1][j];
    return dp[m][m / 2];
}
void process(int tc)
{
    cin >> n >> m;
    for (int i = 1 ; i <= n ; ++i)
        cin >> p[i];
    sort(p + 1 , p + 1 + n);
    double ans = 0;
    for (int l = 0 ; l <= m ; ++l)
    {
        vector<double> a;
        int pt = 1;
        for (int i = 0 ; i < l ; ++i)
            a.push_back(p[pt++]);
        pt = n;
        for (int i = 0 ; i < m - l ; ++i)
            a.push_back(p[pt--]);
        assert(a.size() == m);
        double new_ans = calc(a);
        cerr << "new_ans = " << new_ans << endl;
        ans = max(ans, new_ans);
    }

    cout << "Case #" << tc << ": " << fixed << setprecision(12) << ans << endl;
}


int main()
{
    int t = 0 ;
    cin >> t;
    for (int i = 1 ; i <= t ; ++i)
        process(i);
    return 0;
}
