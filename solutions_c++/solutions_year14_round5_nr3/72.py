#include <bits/stdc++.h>
using namespace std;
#define REC {in = tmpIn; out = tmpOut; u = tmpu;}
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 15;
const int INF = 1e9;
int Tc;
int n;
bool t[N];
int a[N];
int ans;
int u;
set <int> in;
set <int> out;

void dfs(int i) {
    if (i == n) {
        ans = min(ans, (int)in.size() + u);
        return;
    }
    set <int> tmpIn = in;
    set <int> tmpOut = out;
    int tmpu = u;
    if (t[i]) {
        if (a[i] != 0) {
            int x = a[i];
            if (out.count(x)) return;
            out.insert(x);
            bool flag = in.count(x);
            if (flag) {
                in.erase(x);
            } else {
                u = max(u - 1, 0);
            }
            dfs(i + 1);
            REC;
        } else {
            u = max(u - 1, 0);
            dfs(i + 1);
            REC;
            for (auto it = in.begin(); it != in.end(); it++) {
                int x = *it;
                in.erase(x);
                out.insert(x);
                dfs(i + 1);
                it = in.insert(x).first;
                out.erase(x);
            }
        }
    } else {
        if (a[i] != 0) {
            int x = a[i];
            if (in.count(x)) return;
            in.insert(x);
            out.erase(x);
            dfs(i + 1);
            REC;
        } else {
            u++;
            dfs(i + 1);
            u--;
            for (auto it = out.begin(); it != out.end(); it++) {
                int x = *it;
                out.erase(x);
                in.insert(x);
                dfs(i + 1);
                it = out.insert(x).first;
                in.erase(x);
            }
        }
    }
}

int main() {
    cin >> Tc;
    rep (ri, Tc) {
        printf("Case #%d: ", ri + 1);
        cin >> n;
        rep (i, n) {
            char c;
            cin >> c >> a[i];
            t[i] = c == 'L';
        }
        ans = INF;
        u = 0;
        in.clear();
        out.clear();
        dfs(0);
        if (ans == INF) {
            puts("CRIME TIME");
        } else {
            printf("%d\n", ans);
        }
    }
}

