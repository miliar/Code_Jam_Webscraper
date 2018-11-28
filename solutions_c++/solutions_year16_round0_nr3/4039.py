#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

int gDigit = 32;

int powerMod(int base, int power, int divisor) {
    int num = base % divisor;
    int p = 1;
    for (int i=0; i<power; i++) {
        p = p * num;
        p = p % divisor;
    }
    return p;
}

int numDivisor(char r[], int base, int divisor) {
    int res = 0;
    for (int i=0; i<gDigit; i++)
        if (r[i] == '1')
            res = res + powerMod(base, gDigit-i-1, divisor);
    return (res % divisor);
}

int cekJamCoin(char r[], int base) {
    if (numDivisor(r,base,2) == 0) return 2;
    int maks = 500000; //floor(sqrt(num)) + 1;
    for (int i=3; i<=maks; i=i+2)
        if (numDivisor(r,base,i) == 0)
            return i;
    return 0;
}

void dec2bin(char r[], int num) {
    int i = gDigit-1;
    while (num != 0) {
        r[i] = num%2==0 ? '0': '1';
        num /= 2;
        i--;
    }
}

int main() {
    int n, j, maks=16384;
    cin >> n;
    cin >> n; cin >> j;
    cout << "Case #1:\n";
    for (int i=0; i<maks && j>0; i++) {
        char r[] = "10000000000000000000000000000000";
        int res[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        int flag = 0;
        dec2bin(r, (i << 1) + 1);
        for (int base=2; base<11; base++) {
            int bagi = cekJamCoin(r, base);
            if (bagi == 0) break;
            res[base-2] = bagi;
            flag++;
        }
        if (flag == 9) {
            cout << r << " " << res[0];
            for (int base=1; base<9; base++)
                cout << " " << res[base];
            cout << endl;
            j--;
        }
    }
    return 0;
}
