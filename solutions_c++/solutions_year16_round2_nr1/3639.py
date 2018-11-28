#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <array>

using namespace std;

string s;
vector<int> di;

void gen(int prev, vector<int> &d, int stay, string &ans)
{
    if (d.size() == 0) {
        return;
    }
    // cerr << prev << " " << stay << endl;
    if (prev == 10) {
        return;
    }
    if (stay == 0) {
        cout << ans << endl;
        d.resize(0);
        return;
    }
    for (int i = prev; i <= 9; i++) {
        if (i == 0) {
            if (d['Z' - 'A'] >= 1 && d['E' - 'A'] >= 1 && d['R' - 'A'] >= 1 && d['O' - 'A'] >= 1) {
                d['Z' - 'A'] -= 1;
                d['E' - 'A'] -= 1;
                d['R' - 'A'] -= 1;
                d['O' - 'A'] -= 1;
                ans += "0";
                gen(i, d, stay - 4, ans);
                ans.resize(ans.size() - 1);
                d['Z' - 'A'] += 1;
                d['E' - 'A'] += 1;
                d['R' - 'A'] += 1;
                d['O' - 'A'] += 1;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 1) {
            if (d['O' - 'A'] >= 1 && d['N' - 'A'] >= 1 && d['E' - 'A'] >= 1) {
                d['O' - 'A'] -= 1;
                d['N' - 'A'] -= 1;
                d['E' - 'A'] -= 1;
                ans += "1";
                gen(i, d, stay - 3, ans);
                ans.resize(ans.size() - 1);
                d['O' - 'A'] += 1;
                d['N' - 'A'] += 1;
                d['E' - 'A'] += 1;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 2) {
            if (d['T' - 'A'] >= 1 && d['W' - 'A'] >= 1 && d['O' - 'A'] >= 1) {
                d['T' - 'A'] -= 1;
                d['W' - 'A'] -= 1;
                d['O' - 'A'] -= 1;
                ans += "2";
                gen(i, d, stay - 3, ans);
                ans.resize(ans.size() - 1);
                d['T' - 'A'] += 1;
                d['W' - 'A'] += 1;
                d['O' - 'A'] += 1;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 3) {
            if (d['T' - 'A'] >= 1 && d['H' - 'A'] >= 1 && d['R' - 'A'] >= 1 && d['E' - 'A'] >= 2) {
                d['T' - 'A'] -= 1;
                d['H' - 'A'] -= 1;
                d['R' - 'A'] -= 1;
                d['E' - 'A'] -= 2;
                ans += "3";
                gen(i, d, stay - 5, ans);
                ans.resize(ans.size() - 1);
                d['T' - 'A'] += 1;
                d['H' - 'A'] += 1;
                d['R' - 'A'] += 1;
                d['E' - 'A'] += 2;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 4) {
            if (d['F' - 'A'] >= 1 && d['O' - 'A'] >= 1 && d['U' - 'A'] >= 1 && d['R' - 'A'] >= 1) {
                d['F' - 'A'] -= 1;
                d['O' - 'A'] -= 1;
                d['U' - 'A'] -= 1;
                d['R' - 'A'] -= 1;
                ans += "4";
                gen(i, d, stay - 4, ans);
                ans.resize(ans.size() - 1);
                d['F' - 'A'] += 1;
                d['O' - 'A'] += 1;
                d['U' - 'A'] += 1;
                d['R' - 'A'] += 1;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 5) {
            if (d['F' - 'A'] >= 1 && d['I' - 'A'] >= 1 && d['V' - 'A'] >= 1 && d['E' - 'A'] >= 1) {
                d['F' - 'A'] -= 1;
                d['I' - 'A'] -= 1;
                d['V' - 'A'] -= 1;
                d['E' - 'A'] -= 1;
                ans += "5";
                gen(i, d, stay - 4, ans);
                ans.resize(ans.size() - 1);
                d['F' - 'A'] += 1;
                d['I' - 'A'] += 1;
                d['V' - 'A'] += 1;
                d['E' - 'A'] += 1;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 6) {
            if (d['S' - 'A'] >= 1 && d['I' - 'A'] >= 1 && d['X' - 'A'] >= 1) {
                d['S' - 'A'] -= 1;
                d['I' - 'A'] -= 1;
                d['X' - 'A'] -= 1;
                ans += "6";
                gen(i, d, stay - 3, ans);
                ans.resize(ans.size() - 1);
                d['S' - 'A'] += 1;
                d['I' - 'A'] += 1;
                d['X' - 'A'] += 1;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 7) {
            if (d['S' - 'A'] >= 1 && d['V' - 'A'] >= 1 && d['N' - 'A'] >= 1 && d['E' - 'A'] >= 2) {
                d['S' - 'A'] -= 1;
                d['V' - 'A'] -= 1;
                d['N' - 'A'] -= 1;
                d['E' - 'A'] -= 2;
                ans += "7";
                gen(i, d, stay - 5, ans);
                ans.resize(ans.size() - 1);
                d['S' - 'A'] += 1;
                d['V' - 'A'] += 1;
                d['N' - 'A'] += 1;
                d['E' - 'A'] += 2;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 8) {
            if (d['E' - 'A'] >= 1 && d['I' - 'A'] >= 1 && d['G' - 'A'] >= 1 && d['H' - 'A'] >= 1 && d['T' - 'A'] >= 1) {
                d['E' - 'A'] -= 1;
                d['I' - 'A'] -= 1;
                d['G' - 'A'] -= 1;
                d['H' - 'A'] -= 1;
                d['T' - 'A'] -= 1;
                ans += "8";
                gen(i, d, stay - 5, ans);
                ans.resize(ans.size() - 1);
                d['E' - 'A'] += 1;
                d['I' - 'A'] += 1;
                d['G' - 'A'] += 1;
                d['H' - 'A'] += 1;
                d['T' - 'A'] += 1;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
        if (i == 9) {
            if (d['N' - 'A'] >= 2 && d['I' - 'A'] >= 1 && d['E' - 'A'] >= 1) {
                d['N' - 'A'] -= 2;
                d['I' - 'A'] -= 1;
                d['E' - 'A'] -= 1;
                ans += "9";
                gen(i, d, stay - 4, ans);
                ans.resize(ans.size() - 1);
                d['N' - 'A'] += 2;
                d['I' - 'A'] += 1;
                d['E' - 'A'] += 1;
            } else {
                gen(i + 1, d, stay, ans);
            }
        }
    }
}

void solve()
{
    di.assign(26, 0);
    int t = 0;
    for (int i = 0; i < s.length(); i++) {
        di[s[i] - 'A']++;
        t++;
    }
    string ans = "";
    gen(0, di, t, ans);
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        cin >> s;
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}