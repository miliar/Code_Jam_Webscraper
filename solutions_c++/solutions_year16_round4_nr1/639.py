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

string ans;

char get_winner(char a, char b)
{
    if (a == 'P') {
        if (b == 'S') return 'S';
        else return 'P';
    } else if (a == 'S') {
        if (b == 'P') return 'S';
        else return 'R';
    } else if (a == 'R') {
        if (b == 'P') return 'P';
        else return 'R';
    }
}

bool test_match(string s)
{
    if (s.size() == 1) return true;

    string nxt;

    for (int i = 0; i < s.size(); i += 2) {
        if (s[i] == s[i + 1]) {
            return false;
        }

        nxt += get_winner(s[i], s[i + 1]);
    }

    return test_match(nxt);
}

bool gen_all(int r, int p, int s, string pref)
{
    if (r + p + s == 0) {
        if (test_match(pref)) {
            ans = pref;
            return true;
        } else {
            return false;
        }
    }

    if (p > 0 && gen_all(r, p - 1, s, pref + "P")) return true;
    if (r > 0 && gen_all(r - 1, p, s, pref + "R")) return true;
    if (s > 0 && gen_all(r, p, s - 1, pref + "S")) return true;

    return false;
}

string solve(int test)
{
    int n; cin >> n;
    int r, p, s; cin >> r >> p >> s;

    ans = "IMPOSSIBLE";
    gen_all(r, p, s, "");

    return ans;
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int t; cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        cout << solve(t);
        cout << endl;
    }

    return 0;
}
