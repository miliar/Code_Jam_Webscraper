#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

#define pb push_back
const int N = 110;

int n, m, g[N][N];

string solve() {
    cin>>n>>m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &g[i][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            bool f1 = 1, f2 = 1;
            for (int k = 0; k < m && f1; k++) {
                if (g[i][j] < g[i][k]) f1 = 0;
            }
            for (int k = 0; k < n && f2; k++) {
                if (g[i][j] < g[k][j]) f2 = 0;
            }
            if (!f1 && !f2) return "NO";
        }
    }
    return "YES";
}

int main() {
	freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
	int T;
    cin>>T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: %s\n", i, solve().c_str());
    }
}