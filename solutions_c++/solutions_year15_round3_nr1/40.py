#include <iostream>
#include <cstdio>

using namespace std;

int f(int r, int c, int w) {
    if (r == 1) {
        int d = c / w;
        d--;
        d += w;
        if (c % w > 0)
            d++;
        return d;
    } else
        return f(r - 1, c, w) + c / w;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        int r, c, w;
        cin >> r >> c >> w;
        cout << f(r, c, w) << endl;
    }

    return 0;
}
