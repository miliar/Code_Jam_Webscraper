#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

inline bool isPalin(int n) {
    int t=n, nn=0;
    while (t) {
        nn = nn*10 + t%10;
        t /= 10;
    }
    return (nn==n);
}
int main() {
    ifstream cin("in_codejam");
    ofstream cout("out_codejam");
    int T, cases=0;
    long long A, B, n, sum;
    cin >> T;
    while (T--) {
        sum = 0;
        cin >> A >> B;
        for (long long i=A; i<=B; ++i) {
            n = sqrt(i);
            sum += (isPalin(i) && n*n==i && isPalin(n));
        }
        cout << "Case #" << (++cases) << ": " << sum << endl;
    }
    return 0;
}
