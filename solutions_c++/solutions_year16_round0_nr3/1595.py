#include <bits/stdc++.h>

using namespace std;

const int MAXN = 32 + 10;

int a[MAXN];
int n, j;

void init(int _n, int _j) {
    n = _n; j = _j;
}

int convert_to_base(int base, int mod) {
    int x = 0;
    for(int i = 1; i <= n; i++) {
        x = ((x * base) + a[i]) % mod;
    }
    return x;
}

void check() {
    //cout << (convert_to_base(2, 10) != 4) << " " << (convert_to_base(4, 10) != 4) << " " << (convert_to_base(8, 10) != 4) << endl;
    if ((convert_to_base(2, 5) != 0) || (convert_to_base(4, 5) != 0) || (convert_to_base(8, 5) != 0))
        return;

    if ((convert_to_base(3, 2) != 0) || (convert_to_base(5, 2) != 0) || (convert_to_base(7, 2) != 0) || (convert_to_base(9, 2) != 0))
        return;

    int d6 = -1;
    for(int i = 2; i <= 100; i++) {
        if (convert_to_base(6, i) == 0) {
            d6 = i;
            break;
        }
    }
    if (d6 == -1) return;

    j--;
    for(int i = 1; i <= n; i++) cout << a[i]; cout << " ";
    for(int i = 2; i <= 10; i++) {
        if ((i % 2 == 1)) cout << 2;
        else if (i == 6) cout << d6;
        else if (i == 10) cout << 3;
        else cout << 5;
        if (i + 1 <= 10) cout << " ";
    }
    cout << endl;

}

void gen(int p, int left) {
    if (p >= n) {
        if (left == 0) {
            check();
        }
        return;
    }
    if ((n - p + 1) < left) return;
    int s = ((n - p + 1) == left);
    for(int i = s; i <= 1; i++) {
        a[p] = i;
        gen(p + 1, left - (i == 1));
        if (j == 0) return;
    }
}

void solve() {
    a[1] = a[n] = 1;
    gen(2, 10);
    //cout << j << endl;
}

int main()
{
    freopen("C2.out", "w", stdout);

    cout << "Case #1:\n";
    init(32, 500);
    solve();
}
