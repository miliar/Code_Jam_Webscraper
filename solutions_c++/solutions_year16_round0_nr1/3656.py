#include <cstdio>
#include <iostream>
#include <fstream>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

void addDigits(long long num, set<int> &d) {
    while (num > 0) {
        d.insert(num % 10);
        num = num / 10;
    }
}

void solve(ifstream &in, ofstream &out) {
    long long N;
    in >> N;
    set<int> digits;
    long long maximum = max((long long)1000, 100 * N);
    for (long long i = 1; i <= maximum; i++) {
        long long res = i*N;
        addDigits(res, digits);
        if (digits.size() == 10) {
            out << res << endl;
            cout << res << endl;
            return;
        }
    }
    out << "INSOMNIA" << endl;
    cout << "INSOMNIA" << endl;
}

int main() {
    ifstream in("A.in");
    ofstream out("A.txt");
    int T;
    in >> T;
    for (int i = 1; i <= T; i++){
        out << "Case #" << i << ": ";
        cout << "Case #" << i << ": ";
        solve(in, out);
    }
    return 0;
}