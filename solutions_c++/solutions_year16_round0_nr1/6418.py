#include <iostream>
#include <cstdio>
using namespace std;

int check(int n) {
    int mask = 0;
    for (long long i = 0; i < 1000000; i++) {
        long long x = n * i;
        while (x) {
            mask |= 1 << (x % 10);
            x /= 10;
        }
        if (mask == 1023) return n * i;
    }
    return -1;

}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int Tcas;
    cin >> Tcas;
    for (int T = 1; T <= Tcas; T++) {
        int n;
        cin >> n;
        int res = check(n);
        if (res < 0) {
            cout << "Case #" << T << ": INSOMNIA" << endl;
        } else {
            cout << "Case #" << T << ": " << res << endl;
        }
    }
}
