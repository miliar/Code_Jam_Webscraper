#include <cstdio>
#include <iostream>
#include <string>
#include <set>
#include <vector>

using namespace std;

int n, m;
string s[110];
vector<string> a[110];
int ans, cnt;

void go () {
    set<string> S;
    int curr = 0;

    for (int i = 0; i < m; ++i) {
        S.clear();
        for (auto ss : a[i])
            for (int i = 0; i <= (int)ss.size(); ++i)
                S.insert (string(ss.begin(), ss.begin() + i));
        curr += S.size();
    }

    if (curr > ans) {
        ans = curr;
        cnt = 0;
    }
    if (curr == ans)
        ++cnt;
}

void rek (int x) {
    if (x == n) {
        go();
        return;
    }
    for (int i = 0; i < m; ++i) {
        a[i].push_back(s[x]);
        rek(x + 1);
        a[i].pop_back();
    }
}

void solve ()
{
    ans = -1;
    scanf ("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
        cin >> s[i];

    rek (0);
    printf ("%d %d\n", ans, cnt);
}

int main (int argc, char *argv[])
{
    int No; scanf ("%d", &No);
    for (int i = 0; i < No; ++i) {
        if (argc == 1) printf ("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}


