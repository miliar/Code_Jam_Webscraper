#include <bits/stdc++.h>
using namespace std;

long n;

void input()
{
    cin >> n;
}

int occur(long n)
{
    int ret = 0;
    do {
        ret |= 1 << n % 10;
    } while (n /= 10);
    return ret;
}

void solve()
{
    if (n == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }
    int bit = 0;
    for (long t = n; ; t += n) {
        bit |= occur(t);
        if (bit == 1023) {
            cout << t << endl;
            return;
        }
    }
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        input();
        cout << "Case #" << i << ": ";
        solve();
    }
}
