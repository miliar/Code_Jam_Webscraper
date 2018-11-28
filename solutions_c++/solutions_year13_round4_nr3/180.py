#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

const int maxn = 2048;

int A[maxn], B[maxn];
int n;

int g[maxn][maxn];
int in[maxn];
int top[maxn];

int f[maxn];

bool check()
{
    for (int i = 0; i < n; ++i) {
        f[i] = 1;
        for (int j = 0; j < i; ++j) {
            if (top[j] < top[i]) {
                f[i] = max(f[i], f[j] + 1);
            }
        }
        if (f[i] != A[i]) {
            return false;
        }
    }
    for (int i = n - 1; i >= 0; --i) {
        f[i] = 1;
        for (int j = i + 1; j < n; ++j) {
            if (top[j] < top[i]) {
                f[i] = max(f[i], f[j] + 1);
            }
        }
        if (f[i] != B[i]) {
            return false;
        }
    }
    return true;
}

void solve() 
{
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &A[i]);
    }
    for (int i = 0; i < n; ++i) {
        scanf("%d", &B[i]);
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            g[i][j] = 0;
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (A[i] >= A[j]) {
                g[j][i] = 1;
            }
            if (B[i] <= B[j]) {
                g[i][j] = 1;
            }
        }

        for (int j = i - 1; j >= 0; --j) {
            if (A[j] + 1 == A[i]) {
                g[j][i] = 1;
                break;
            }
        }

        for (int j = i + 1; j < n; ++j) {
            if (B[j] + 1 == B[i]) {
                g[j][i] = 1;
                break;
            }
        }
    }

    memset(in, 0, sizeof in);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (g[i][j]) {
                in[j]++;
            }
        }
    }

    priority_queue<int> q;
    for (int i = 0; i < n; ++i) {
        if (in[i] == 0) {
            q.push(-i);
        }
    }

    int cnt = 0;
    while (!q.empty()) {
        int x = -(q.top()); q.pop();
        for (int i = 0; i < n; ++i) {
            if (g[x][i]) {
                in[i]--;
                if (in[i] == 0) {
                    q.push(-i);
                }
            }
        }
        top[x] = ++cnt;
    }

    if (!check()) {
        cout << "ERROR";
    }

    for (int i = 0; i < n; ++i) {
        printf(" %d", top[i]);
    }
    puts("");
}

int main() {
    freopen("C-large.in", "r", stdin);
    //freopen("C-small-attempt2.in", "r", stdin);
    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; ++_) {
        printf("Case #%d:", _);
        solve();
    }
}


