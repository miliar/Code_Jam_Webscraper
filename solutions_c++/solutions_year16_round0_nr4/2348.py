#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

unsigned long long pow(unsigned long long b, unsigned long long n) {
    unsigned long long res = 1;
    for (unsigned long long i=0; i<n; i++) {
        res *= b;
    }
    return res;
}

int main () {
    unsigned long long m;
    cin >> m;
    for (unsigned long long i=0; i<m; i++) {
        cout << "Case #" << i+1 << ": ";
        unsigned long long k, c, s;
        cin >> k >> c >> s;
        if (k == 1) {
            cout << 1 << endl;
            continue;
        }
        unsigned long long j;
        for (j = 1; j<s; j++) {
            cout << (k-j)*((pow(k, c) - 1)/(k-1)) + 1 << " ";
        }
        cout << 1 << endl;
    }
    return 0;
}
