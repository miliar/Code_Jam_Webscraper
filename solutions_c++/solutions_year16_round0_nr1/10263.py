#include <bits/stdc++.h>
using namespace std;

int relax(int d, vector<int>& mark) {
    int cnt = 0;
    if (d == 0) {
        cnt += mark[0] == false;
        mark[0] = true;
    }

    while (d > 0) {
        cnt += mark[d % 10] == false;
        mark[d % 10] = true;
        d /= 10;
    }

    return cnt;
}

void solve() {
    int n;
    cin >> n;

    if (n == 0) {
        printf("INSOMNIA\n");
        return;
    }

    int d = n;
    vector<int> mark(10, false);
    int cnt = relax(n, mark);
    while (cnt < 10) {
        d += n;
        cnt += relax(d, mark);
    }

    printf("%d\n", d);
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    } 
}

