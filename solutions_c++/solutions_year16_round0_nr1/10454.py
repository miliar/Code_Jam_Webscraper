#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

typedef unsigned int uint;

uint countDigits(uint k) {
    return k ? 1 + countDigits(k/10) : 0;
}

uint maxElement(uint k) {
    return k ? 10 * maxElement(--k) : 1;
}

int main() {
    freopen("A-large.in", "r",stdin);
    freopen("A-large.out", "w",stdout);
    int t, sum, i,j;
    uint n, maxN, l, k;
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
