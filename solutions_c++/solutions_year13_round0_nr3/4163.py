#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream fin("fair.in");
ofstream fout("fair.out");

const int MAXN = 100000;
const long long limit = 100000000000000;

long long palim[MAXN];

bool isPalindrom(long long n) {
    int cif[20]; cif[0] = 0;

    while (n) {
        cif[++cif[0]] = n % 10;
        n /= 10;
    }

    for (int i = 1; i <= cif[0] / 2; ++i)
        if (cif[i] != cif[cif[0] - i + 1])
            return 0;
    return 1;
}

void genData() {
    for (int i = 1; 1LL * i * i <= limit; ++i) {
        //cerr << i;
        if (isPalindrom(1LL * i * i) && isPalindrom(i))
            palim[++palim[0]] = 1LL * i * i;
    }
}

int main() {
    genData();
    int t; fin >> t;
    for (int i = 1; i <= t; ++i) {
        long long a, b;
        fin >> a >> b;
        fout << "Case #" << i << ": " << upper_bound(palim + 1, palim + palim[0] + 1, b) - lower_bound(palim + 1, palim + palim[0] + 1, a) << "\n";
    }
    return 0;
}
