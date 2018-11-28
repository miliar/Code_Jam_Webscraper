#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <cmath>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

#define X first
#define Y second

const int INF = (1<<30);
int a[20][20], r, c, n, ans;

int calc() {
    int res = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            res += (a[i][j] == 1 && a[i + 1][j] == 1);
            res += (a[i][j] == 1 && a[i][j + 1] == 1);
        }
    }
    return res;
}

void rec(int x, int y, int t) {
    if (x == r) {
        if (t == n) {
            /*for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    cerr<<a[i][j];
                }
                cerr<<endl;
            }
            cerr<<calc()<<endl;*/
            ans = min(ans, calc() );
        }
        return ;
    }
    int tox, toy;
    if (y == c - 1) {
        tox = x + 1; toy = 0;
    }
    else {
        tox = x; toy = y + 1;
    }
    rec(tox, toy, t);
    if (t < n) {
        a[x][y] = 1;
        rec(tox, toy, t + 1);
        a[x][y] = 0;
    }
}

int solve() {
    ans = INF;
    cin>>r>>c>>n;
    rec(0, 0, 0);
    return ans;
}

int main() {
    freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    int test;
    cin>>test;
    for (int i = 1; i <= test; i++) {
        printf("Case #%d: %d\n", i, solve() );
    }

    return 0;
}
