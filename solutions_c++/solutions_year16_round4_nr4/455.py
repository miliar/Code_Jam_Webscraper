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

#define MAXN 500006
#define MOD 1000000007

string solve(int test)
{

    return "";
}

bool is_good(vector<string> var)
{
    unordered_map<string, int> q;
    for (auto &s : var) {
        q[s]++;
    }

    for (auto &p : q) {
        int ones = 0;
        for (auto c : p.first) {
            ones += c == '1';
        }
        if (ones != p.second) {
            return false;
        }
    }


    for (int i = 0; i < var.size(); ++i) {
        for (int j = i; j < var.size(); ++j) {
            swap(var[i][j], var[j][i]);
        }
    }

    q.clear();
    for (auto &s : var) {
        q[s]++;
    }

    for (auto &p : q) {
        int ones = 0;
        for (auto c : p.first) {
            ones += c == '1';
        }
        if (ones != p.second) {
            return false;
        }
    }

    return true;
}

int solve_rec(int i, int j, int n, int score, vector<string>& var)
{
    if (j == n) {
        ++i;
        j = 0;
    }

    if (i == n) {
        if (is_good(var)) {
//            cout << score << endl; for (auto &s : var) cout << s << endl; cout << endl;
            return score;
        } else {
            return n * n;
        }
    }


    if (var[i][j] == '1') {
        return solve_rec(i, j + 1, n, score, var);
    } else {
        int result = n * n;
        result = min(result, solve_rec(i, j + 1, n, score, var));
        var[i][j] = '1';
        result = min(result, solve_rec(i, j + 1, n, score + 1, var));
        var[i][j] = '0';
        return result;
    }

}

int solve_brute(int test)
{
    int n; cin >> n;

    vector<string> vs(n);
  //  cout << endl;
    for (int i = 0; i < n; ++i) {
        cin >> vs[i];
//        cout << vs[i] << endl;
    }

    int result = n * n;
    /*
       for (int mask = 0; mask <= (1 << (n * n)); ++mask) {
       int mask_score = 0;

       vector<string> opt;

       for (int j = 0; j < n * n; ++j) {
       int b = (mask & (1 << j)) != 0;

       if (b == 0 && vs[j / n][j % n] == '1') {
       mask_score = -1;
       break;
       }

       if (b == 1 && vs[j / n][j % n] == '0') {
       ++mask_score;
       }

       }

       if (mask_score == -1) {
       continue;
       }
       }
       */
    //    return 0;

    return solve_rec(0, 0, n, 0, vs);
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int t; cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        cout << solve_brute(t);
        cout << endl;
    }

    return 0;
}
