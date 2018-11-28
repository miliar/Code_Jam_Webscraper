#include <iostream>
#include <stdio.h>
#include <cmath>

using namespace std;

int t, k, c, cnt;
long long s, pos;


long long get_pos(long long prev, long long cur) {
    long long ans = 1;
    long long kpow = 1;
    for (long long i = cur - prev; i < c; ++i)
        kpow *= k;
    for (long long i = cur; i > prev; --i) {
        ans += kpow * (i - 1);
        kpow *= k;
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> k >> c >> s;
        pos = 0;
        cnt = k;
        cout << "Case #" << i << ": ";
        if (k > s * c) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        long long pcheck = 0, check = 0;
        while (cnt > 0) {
            cout << (check = get_pos(pos, pos + min(c, cnt))) << ' ';
            if (check < pcheck) {
                cout << "EBAT";
                return 0;
            }
            pcheck = check;
            cnt -= c;
            pos += c;
        }
        cout << endl;
    }
}
