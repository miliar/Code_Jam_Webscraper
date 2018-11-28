#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <array>

using namespace std;

int n;
vector<int> f;

int ans;

void check(vector<int> &d)
{
    vector<int> cur;
    for (int i = 0; i < d.size() && d[i] >= 0; i++) {
        cur.push_back(d[i]);
    }
    for (int i = 0; i < cur.size(); i++) {
        int left;
        int right;
        if (i == 0) {
            left = cur.back();
        } else {
            left = cur[i - 1];
        }
        if (i == cur.size() - 1) {
            right = cur[0];
        } else {
            right = cur[i + 1];
        }
        if (f[cur[i]] != left && f[cur[i]] != right) {
            return;
        }
    }
    if (ans < cur.size()) {
        ans = cur.size();
    }
}

void gen(vector<char> &u, vector<int> &d, int pos, int prev)
{
    // if (d.size() == 0) {
    //     return;
    // }
    if (prev == -10) {
        check(d);
        return;
    }
    for (int i = 0; i < n; i++) {
        if (!u[i]) {
            d[pos] = i;
            u[i] = 1;
            gen(u, d, pos + 1, i);
            u[i] = 0;
        }
    }
    d[pos] = -10;
    gen(u, d, pos + 1, -10);
}

void solve()
{
    vector<char> u(n, 0);
    vector<int> d(n + 1, -2);
    ans = 0;
    gen(u, d, 0, -1);
    cout << ans << endl;
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        f.resize(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &f[i]);
            f[i]--;
        }
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}