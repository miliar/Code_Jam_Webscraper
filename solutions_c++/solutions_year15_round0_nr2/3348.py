#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

const int MAXN = 1111;
const int MAXX = 1111;

int a[MAXN];

int platesCount(int a, int b) {
    int z = a / b;
    if (z * b < a)
        z++;
    return z;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin >> t;

    int k = 0;
    while (k < t) {
        k++;
        cout << "Case #" << k << ": ";
        int n;
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> a[i];

        int res = -1;
        for (int x = 1; x <= MAXX; x++) {
            int d = x;
            for (int i = 0; i < n; i++)
                d += platesCount(a[i], x) - 1;
            if (res < 0 || res > d)
                res = d;
        }
        cout << res << endl;
    }

    return 0;
}
