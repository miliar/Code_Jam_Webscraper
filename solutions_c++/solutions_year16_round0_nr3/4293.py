#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

#define long long long
#define append push_bask

bool EZGet(long mask, int idx) {
    return ((1LL << idx) & mask) > 0;
}

int EZTopIdx(long mask) {
    for (int i = 60; i >= 0; --i) {
        if (EZGet(mask, i)) return i;
    }
    return 0;
}

bool EZIsJamcoin(long mask, int len) {
    return EZGet(mask, 0) && EZTopIdx(mask) == len - 1;
}

string EZBinaryString(long mask) {
    string res = "";
    for (int i = EZTopIdx(mask); i >= 0; --i) {
        res += (char) (EZGet(mask, i) + '0');
    }
    return res;
}

long EZPow(long a, int n) {
    long res = 1;
    for (int i = 0; i < n; ++i) {
        res *= a;
    }
    return res;
}

long EZNumFromStr(long mask, int base) {
    long res = 0;
    for (int i = 0; i < 60; ++i) {
        res += EZGet(mask, i) * EZPow(base, i);
    }
    return res;
}

#define EZ_NO_DIVISOR -1

long EZFindDivisor(long n) {
    for (long i = 2; i * i <= n; ++i) {
        if (n % i == 0) return i;
    }
    return EZ_NO_DIVISOR;
}


int main() {
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        int n, j;
        cin >> n >> j;
        cout << "Case #1:" << endl;

        int cnt = 0;
        for (long mask = 0; mask < (1LL << (n + 1)) && cnt < j; ++mask) {
            if (EZIsJamcoin(mask, n)) {
                string bin = EZBinaryString(mask);

                bool ok = true;
                vector<long> divs(9);
                for (int base = 2; base <= 10; ++base) {
                    long x = EZNumFromStr(mask, base);
                    long div = EZFindDivisor(x);
                    if (div == EZ_NO_DIVISOR) {
                        ok = false;
                        break;
                    } else {
                        divs[base] = div;
                    }
                }

                if (ok) {
                    ++cnt;
                    cout << bin << " ";
                    for (int i = 2; i <= 10; ++i) {
                        cout << divs[i] << " ";
                    }
                    cout << endl;
                }
            }
        }
    }
    return 0;
}