#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

typedef unsigned int uint;
typedef long long unsigned int lluint;

uint countDigits(uint k) {
    return k ? 1 + countDigits(k/10) : 0;
}

lluint maxElement(lluint k) {
    return k ? 10 * maxElement(--k) : 1;
}

int main() {
    freopen("A-large.in", "r",stdin);
    freopen("A-large.out", "w",stdout);
    uint t, sum, i,j;
    lluint n, maxN, l, k;
    cin >> t;
    for(i = 1; i <= t; i++) {
        cin >> n;
        bool b[10] = {false};
        maxN = maxElement(countDigits(n)) * 10;
        for(k = 1; k <= maxN; k++) {
            l = k * n;
            while(l > 0) {
                b[l%10] = true;
                l/=10;
            }
            for(sum = j = 0; j < 10; j++) {
                sum += b[j];
            }
            if (sum == 10) {
                cout << "Case #" << i << ": " << k*n << endl;
                break;
            }
        }
        if (k > maxN)
            cout << "Case #" << i << ": INSOMNIA" << endl;
    }
}
