#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
using namespace std;


#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>

string s[10];
int n, m;
int group[10];
int cans = 0, canss; 
pair<int, string> ss[10];

int preff(string & s1, string & s2) {
    int i = 0;
    while (i < s1.length() && i < s2.length() && s1[i] == s2[i])
        i++;
    return i;
}

bool usd[10];

void check() {
    memset(usd, 0, sizeof usd);
    for (int i = 0; i < m; i++)
        usd[group[i]] = true;
    for (int i = 0; i < n; i++)
        if (!usd[i]) return;
    for (int i = 0; i < m; i++) {
       ss[i] = mp(group[i], s[i]); 
    }
    sort(ss, ss + m);
    int ans = n;
    for (int i = 0; i < m; i++) {
       if (i == 0 || ss[i - 1].first != ss[i].first) {
           ans += ss[i].second.length();
       } else 
           ans += ss[i].second.length() - preff(ss[i - 1].second, ss[i].second);
    }
    if (cans < ans) {
        cans = ans;
        canss = 1;
    } else 
    if (cans == ans) {
        canss++;
    }
}

void bf(int p) {
    if (p == m) {
        check();
        return;
    }
    for (int i = 0; i < n; i++) {
        group[p] = i;
        bf(p + 1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int t; cin >> t;
    for (int ii = 0; ii < t; ii++) {
        cin >> m >> n;
        for (int i = 0; i < m; i++) {
            cin >> s[i];
        }
        cans = 0;
        bf(0);
        cout << "Case #" << ii + 1 << ": " << cans << " " << canss << endl;
    }
}
