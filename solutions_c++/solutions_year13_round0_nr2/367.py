#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <iomanip>
using namespace std;

typedef long long LL;

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

int lawn[111][111];
int n, m;

bool ok(int a, int b) {
    // check row
    bool ok = true;
    int cur = lawn[a][b];
    for (int j = 0; j < m; j++) {
        if (lawn[a][j] > cur) ok = false;
    }
    if (ok) return true;
    // check row
    ok = true;
    for (int i = 0; i < n; i++) {
        if (lawn[i][b] > cur) ok = false;
    }
    if (ok) return true;
    return false;
}

bool isPossible() {
    bool pos = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!ok(i, j)) pos = false;
        }
    }
    return pos;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d", &lawn[i][j]);
            }
        }
        printf("Case #%d: ",tt);
        if (isPossible()) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
	return 0;
}
