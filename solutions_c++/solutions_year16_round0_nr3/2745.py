/*
* @Author: Yinlong Su
* @Date:   2016-04-08 18:46:52
* @Last Modified by:   Yinlong Su
* @Last Modified time: 2016-04-08 22:02:16
*/

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

void coin(ULL n) {
    if (n) {
        coin(n / 2);
        if (n % 2)
            cout << "1";
        else
            cout << "0";
    }
}

ULL n2dec(ULL n, int base) {
    ULL k = 1, r = 0;
    while (n) {
        r += k * (n % 2);
        k *= base;
        n /= 2;
    }
    return r;
}

ULL n2divisor(ULL n) {
    for (ULL i = 2; i <= sqrt(n); i++)
        if (n % i == 0)
            return i;
    return 0;
}

int main(){
    FILE *fin = freopen("C-small-attempt0.in", "r", stdin);
    FILE *fout = freopen("C-small-attempt0.out", "w", stdout);

    ULL T, N, J;
    cin >> T >> N >> J;

    ULL divisor[11];
    ULL b = pow(2, N - 1) + 1, C = 0;

    cout << "Case #1:" << endl;

    for (ULL i = 0; i < pow(2, N - 2); i++) {
        int flag = 1;
        ULL n = b + i * 2;
        memset(divisor, 0, 11 * sizeof(ULL));
        for (int j = 2; j <= 10; j++) {
            ULL k = n2dec(n, j);
            divisor[j] = n2divisor(k);
            if (divisor[j] == 0) {
                flag = 0;
                break;
            }
        }
        if (flag) {
            coin(n);
            for (int j = 2; j <= 10; j++)
                cout << " " << divisor[j];
            cout << endl;
            C++;
        }
        if (C == J)
            break;
    }
    return 0;
}