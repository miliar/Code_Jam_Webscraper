#include <bits/stdc++.h>
#define int long long

using namespace std;

int n;
int cnt, j;
vector <int> ans[600];
string res[600];

int div(int t) {
    int p = t;
    for (int i = 2; i * i <= t; i++) {
        if (t % i == 0) {
            while (t % i == 0) {
                t /= i;
            }
            return i;
        }
    }
    if (t == 1 || t == p) {
        return 0;
    } else {
        return t; 
    }
}

void check(string mask) {
    cnt++;
    int d[11]; 
    memset(d, 0, sizeof d);
    for (int i = 0; i < n; i++) {
        for (int t = 2; t <= 10; t++) {
            d[t] = d[t] * t + (mask[i] - '0');
        }
    }
    bool bad = false;
    vector <int> dg;
    for (int t = 2; t <= 10; t++) {
        int p = div(d[t]);
        if (p != 0) {
            dg.push_back(p); 
        } else {
            bad = 1;
            break;
        }        
    }
    if (!bad) {
        res[cnt] = mask;
        ans[cnt] = dg;
    } else {
        cnt--;
    }
}

void rec(string mask, int len) {
    if (len == n) {
        if (cnt < j) {
            check(mask);
        }
    } else if (len == n - 1) {
        rec(mask + '1', len + 1);
    } else {
        rec(mask + '1', len + 1);
        rec(mask + '0', len + 1);
    }
}

main() {
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    cin >> n >> j;
    rec("1", 1);
    cout << "Case #1:" << endl;
    for (int i = 1; i <= j; i++) {
        cout << res[i] << " ";
        for (int t = 2; t <= 10; t++) {
            cout << ans[i][t - 2] << " ";
        }
        cout << endl;
    }
}
