#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>

using namespace std;

const int MAXN = 1000111;

int f[MAXN];
queue <int> q;

int reverse(int x) {
    int y = 0;
    while (x > 0) {
        y *= 10;
        y += (x % 10);
        x /= 10;
    }
    return y;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin >> t;

    f[1] = 1;
    q.push(1);

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        if (x < MAXN && !f[x + 1]) {
            f[x + 1] = 1 + f[x];
            q.push(x + 1);
        }

        int y = reverse(x);
        if (y < MAXN && !f[y]) {
            f[y] = 1 + f[x];
            q.push(y);
        }
    }

    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        int n;
        cin >> n;
        cout << f[n] << endl;
    }
    return 0;
}
