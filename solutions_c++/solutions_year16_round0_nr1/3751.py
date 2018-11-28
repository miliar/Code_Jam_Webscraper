#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <ctime>
#define LL long long
using namespace std;

const int N = 1000100;

LL res[N];

int main () {
    freopen ("A-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);
    for (int i = 1; i < N; i++) {
        int st = 0;
        for (int j = i; ; j += i) {
            int t = j, an = 0;
            while (t) {
                st |= (1 << t % 10);
                t /= 10;
            }
            if (st == (1 << 10) - 1) { res[i] = j; break; }
        }
    }
    int T, cas = 1;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        printf ("Case #%d: ", cas++);
        if (n == 0) cout << "INSOMNIA" << endl;
        else cout << res[n] << endl;
    }
}
