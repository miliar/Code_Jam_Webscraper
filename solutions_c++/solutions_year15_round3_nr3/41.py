#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

const int MAXN = 111;

long long a[MAXN];
long long c, d, v;

int qwe() {
    long long x = 0;
    long long i = 0;
    int j = 0;
    while (i < v) {
        long long I = i + 1;
        if (j < d && a[j] <= I) {
            i += (a[j] * c);
            j++;
        } else {
            x++;
            i += (I * c);
        }
    }
    return x;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        cin >> c >> d >> v;
        for (int i = 0; i < d; i++)
            cin >> a[i];
        sort(a, a + d);

        cout << qwe() << endl;
    }

    return 0;
}
