#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef unsigned long long llu;

const int MAX = 1e2 + 7;

int main () {
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);
    int t;
    cin >> t;

    for (int kase = 1; kase <= t; kase++) {
        char pancake [MAX], previ = '+';
        int cnt = 0;
        cin >> pancake;

        for (int i = 0; pancake [i]; i++) {
            if (pancake [i] != previ) cnt++;
            previ = pancake [i];
        }
        if (cnt && previ == '+') cnt--;
        if (cnt && pancake [0] == '+') cnt++;

        printf ("Case #%d: %d\n", kase, cnt);
    }

    return 0;
}
