#include <bits/stdc++.h>

using namespace std;

const int N = 15;
const int J = 50;

long long num(int base, int i) {
    long long t = 1;
    long long ans = 0;
    while (i) {
        if (i & 1) {
            ans += t;
        }
        t *= base;
        i >>= 1;
    }
    return ans;
}

int get_divisor(long long num) {
    double tmp = sqrt(num);
    for (int i = 2; i <= tmp; i++) {
        if (num % i == 0) {
            return i;
        }
    }
    return -1;
}

int frame = 1 + (1 << 15);
int divi[11];

int main()
{
    freopen("1.txt", "wt", stdout);
    cout << "Case #1:\n";
    int cnt = 0;
    for (int i = 0; i < 1 << 14; i++) {
        int t = frame + (i << 1);
        bool ok = true;
        for (int base = 2; base <= 10; base++) {
            divi[base] = get_divisor(num(base, t));
            if (divi[base] == -1) {
                ok = false;
                break;
            }
        }
        cerr << i << '\n';
        if (ok) {

            cnt++;
            cout << num(10, t) << ' ';
            for (int i = 2; i <= 10; i++) {
                cout << divi[i] << ' ';
            }
            cout << '\n';
        }
        if (cnt == 50) {
            return 0;
        }
    }
    return 0;
}
