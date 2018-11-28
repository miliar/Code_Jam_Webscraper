#include <bits/stdc++.h>

using namespace std;

#define NMAX 1000001

int D[NMAX], T;

int get_rev(int x) {
    int rev = 0;
    while(x) {
        rev = rev * 10 + x % 10;
        x /= 10;
    }
    return rev;
}

int main() {
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#endif
    
    cin.sync_with_stdio(0);

    cin >> T;

    for (int i = 1, q; i < NMAX; i++) {
        int rev = get_rev(i);
        D[i] = D[i-1] + 1;
        if (rev < i && get_rev(rev) == i)
            D[i] = min(D[i], D[rev] + 1);
    }

    for (int t = 1; t <= T; t++) {
        int q;
        cin >> q;
        cout << "Case #" << t << ": " << D[q] << "\n";
    }

    return 0;
}
