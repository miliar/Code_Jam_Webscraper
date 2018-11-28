#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <cmath>
using namespace std;

ofstream out("d_large.out");

int d(long long k, long long c, long long s) {
    if (s<ceil((double)k/c)) {
        out << "IMPOSSIBLE";
        return 0;
    }
    long long cur = 0;
    long long depth = 0;
    for (long long i = 0; i < k; i++) {
        cur *= k;
        cur += i;
        if (++depth>=c) {
            depth = 0;
            out << cur+1 << " ";
            cur = 0;
        }
    }
    while (depth<c && depth != 0) {
        cur *= k;
        cur += k-1;
        depth++;
    }
    if (depth==c) out << cur+1;
}

int main() {
    ifstream in("D-large.in");
    int n;
    in >> n;
    for (int i = 0; i < n; i++) {
        long long k, c, s;
        in >> k >> c >> s;
        out << "Case #" << i+1 << ": ";
        d(k, c, s);
        out << endl;
    }
}
