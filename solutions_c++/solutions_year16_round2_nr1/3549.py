#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
//#include <unordered_map>

using namespace std;

#define pb push_back
#define all(v) (v).begin(), (v).end()

const string num[10] = {
"ZERO", "ONE", "TWO", "THREE",
"FOUR", "FIVE", "SIX", "SEVEN",
"EIGHT", "NINE"
};

const int dif[5] = {1, 3, 5, 7, 9};

inline bool contain(int n, string &text) {
    string cur = num[n];
    sort(all(cur));
    for (int i = 0; i < (int)cur.size(); i++) {
        if (upper_bound(all(text), cur[i]) - lower_bound(all(text), cur[i]) <
        upper_bound(all(cur), cur[i]) - lower_bound(all(cur), cur[i]))
            return false;
    }
    return true;
}

//unordered_map<string, bool> memo[6];

bool solve(int p, string s, vector<int> &ans) {
    if (p == 5) return s.empty();

    //if (memo[p].count(s)) return memo[p][s];

    if (solve(p+1, s, ans))
        return true;

    int c = dif[p];
    string cur = s;
    if (contain(c, cur)) {
        for (int i = 0; i < (int)num[c].size(); i++)
            cur.erase(lower_bound(all(cur), num[c][i]));
        if (solve(p, cur, ans)) {
            ans.pb(c);
            return true;
        }
    }

    return false;
}

int main() {
    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A-small.out", "wt", stdout);

    int t, tc = 1;
    string s;

    cin >> t;

    while (t--) {
        cin >> s;
        sort(all(s));
        vector<int> ans;
        int c = 0;
        while (contain(c, s)) {
            for (int i = 0; i < (int)num[c].size(); i++)
                s.erase(lower_bound(all(s), num[c][i]));
            ans.pb(c);
        }
        c = 2;
        while (contain(c, s)) {
            for (int i = 0; i < (int)num[c].size(); i++)
                s.erase(lower_bound(all(s), num[c][i]));
            ans.pb(c);
        }
        c = 4;
        while (contain(c, s)) {
            for (int i = 0; i < (int)num[c].size(); i++)
                s.erase(lower_bound(all(s), num[c][i]));
            ans.pb(c);
        }
        c = 6;
        while (contain(c, s)) {
            for (int i = 0; i < (int)num[c].size(); i++)
                s.erase(lower_bound(all(s), num[c][i]));
            ans.pb(c);
        }
        c = 8;
        while (contain(c, s)) {
            for (int i = 0; i < (int)num[c].size(); i++)
                s.erase(lower_bound(all(s), num[c][i]));
            ans.pb(c);
        }
        solve(0, s, ans);
        sort(all(ans));
        cout << "Case #" << tc << ": ";
        tc++;
        for (int i = 0; i < (int)ans.size(); i++)
            cout << ans[i];
        cout << endl;
    }

    return 0;
}
