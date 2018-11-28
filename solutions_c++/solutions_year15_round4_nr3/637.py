#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
using namespace std;

int mp[10333];
int h[3][10333];
int n;
int ans;
vector<string> a[222];

unordered_map<string, int> num;

int d[222];
vector<int> b[222];
int res;

void add(int x, int y) {
    for (int& s : b[x]) {
        h[y][s]++;
        if (h[y][s] == 1 && h[3 - y][s] > 0) {
            res++;
        }
    }
}

void del(int x, int y) {
    for (int& s : b[x]) {
        h[y][s]--;
        if (h[y][s] == 0 && h[3 - y][s] > 0) {
            res--;
        }
    }
}



void rec(int x) {
    if (res >= ans) {
        return;
    }
    if (x == n + 1) {
        if (res < ans) {
            ans = res;
        }
        return;
    }
    if (x == 1) {
        add(x, 1);
        rec(x + 1);
        del(x, 1);
        return;
    }
    if (x == 2) {
        add(x, 2);
        rec(x + 1);
        del(x, 2);
        return;
    }
    int o = res & 1;
    add(x, 1 + o);
    rec(x + 1);
    del(x, 1 + o);
    add(x, 2 - o);
    rec(x + 1);
    del(x, 2 - o);
}


void renum() {
    int x = 0;
    num.clear();
    for (int i = 1; i <= n; i++) {
        b[i].clear();
        for (string& s : a[i]) {
            if (num[s] == 0) {
                num[s] = ++x;
            }
            b[i].push_back(num[s]);
        }
    }
}

void solve() {
    cin >> n;
    ans = 1 << 30;
    for (int i = 1; i <= n; i++) {
        a[i].clear();
        while (true) {
            string s;
            cin >> s;
            a[i].push_back(s);
            char q = getchar();
            if (q == '\n') {
                break;
            }
        }
    }
    renum();
    int toAdd = 0;
    memset(mp, 0, sizeof(mp));
    for (int i = 1; i <= 2; i++) {
        for (int& s : b[i]) {
            mp[s] |= i;
        }
    }
    for (int p = 0; p <= 10000; p++) {
        if (mp[p] == 3) {
            toAdd++;
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j < int(b[i].size()); j++) {
                    if (p == b[i][j]) {
                        swap(b[i][j], b[i][int(b[i].size()) - 1]);
                        b[i].pop_back();
                    }
                }
            }
        }
    }
    cerr << toAdd << endl;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < int(b[i].size()); j++) {
            int cnt = 0;
            for (int i1 = 1; i1 <= n; i1++) {
                for (int j1 = 0; j1 < int(b[i1].size()); j1++) {
                    if (b[i][j] == b[i1][j1]) {
                        cnt++;
                        break;
                    }
                }
            }
            if (cnt == 1) {
                swap(b[i][j], b[i][int(b[i].size()) - 1]);
                b[i].pop_back();
            }
        }
    }
    cerr << b[1].size() << " " << b[2].size() << endl;
    res = 0;
    rec(1);
    printf("%d\n", ans + toAdd);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int test = 1; test <= tc; test++) {
        printf("Case #%d: ", test);
        cerr << test << endl;
        solve();
    }
    return 0;
}