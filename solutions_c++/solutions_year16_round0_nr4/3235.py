#include <iostream>

using namespace std;
long long T;
long long N, I, S;
long long pow(long long n, long long p) {
    long long v = 1;
    for(long long i = 0; i < p; i++) {
        v *= n;
    }
    //cerr << "Pow" << n << " " << p << " " << v << "\n";
    return v;
}

int main() {
    cin >> T;
    for(long long t = 1; t <= T; t++) {
        cin >> N >> I >> S;
        cout << "Case #" << t << ":";
        long long d = pow(N, I-1);
        for(long long i = 0; i < S; i++) {
            cout << " " << d*i+1ll;
        }
        cout << "\n";
    }
    return 0;
}
