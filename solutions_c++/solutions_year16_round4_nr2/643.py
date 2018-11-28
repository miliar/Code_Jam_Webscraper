#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <deque>
#include <ctime>
#include <cstring>
#include <unordered_map>
#include <unordered_set>

//#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

#define forr(i, n) for(ll (i) = 0LL; (i) < (n); (i)++)

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> plll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;
typedef vector < pll > vll;

int INT_MAX_VAL = (int)  0x3F3F3F3F;
int INT_MIN_VAL = (int) -0x3F3F3F3F;
ll LONG_MAX_VAL = (ll)   0x3F3F3F3F3F3F3F3F;
ll LONG_MIN_VAL = (ll)  -0x3F3F3F3F3F3F3F3F;

#define MAXN 205
#define MOD 1000000007
#define MIDK 205
#define MAXK (MIDK*2 + 10)

long double dp[MAXN][MAXK];

double find_tie(vector<double> ds, int k)
{
    for (int i = 0; i < MAXN; ++i) {
        for (int j = 0; j < MAXK; ++j) {
            dp[i][j] = 0;
        }
    }

    dp[0][MIDK] = 1.;
    for (int i = 0; i < ds.size(); ++i) {
        for (int j = -k; j <= k; ++j) {
            dp[i + 1][MIDK + j + 1] += dp[i][MIDK + j] * ds[i];
            dp[i + 1][MIDK + j - 1] += dp[i][MIDK + j] * (1. - ds[i]);
//            cout << ds[i] << " " << i + 1 << " " << MIDK + j << endl;
        }
    }

    return dp[ds.size()][MIDK];
}

double solve(int test)
{
    int n, k; cin >> n >> k;
    vector<double> ds(n);
    for (int i = 0; i < n; ++i) {
        cin >> ds[i];
    }

    sort(ds.begin(), ds.end());

    double result = 0;

    for (int i = 0; i <= k; ++i) {
        vector<double> cand;
        for (int j = 0; j < i; ++j) {
            cand.push_back(ds[j]);
        }

        for (int j = n - k + i; j < n; ++j) {
            cand.push_back(ds[j]);
        }

        double cur_res = find_tie(cand, k);
        result = max(result, cur_res);
    }

    return result;
}

int main()
{
//    cin.tie(0);
//    ios::sync_with_stdio(false);

    int t; cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        cout << fixed << setprecision(9) << solve(t);
        cout << endl;
    }

    return 0;
}
