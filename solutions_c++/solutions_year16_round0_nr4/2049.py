#include <iostream>
#include <set>
using namespace std;

long long power(long long base, long long expo) {
    if(expo == 0) return 1;
    else return base * power(base, expo - 1);
    
}

long long f(long long k, long long c, long long s) {
    if(c == 1) return s;
    else return s * power(k, c - 1) + f(k, c - 1, (s + 1) % k);
}

int main() {
    int t; cin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        long long k, s, c; cin >> k >> c >> s;
        cout << "Case #" << tt << ": ";
        if(c * s < k) {
            cout << "IMPOSSIBLE\n";
            continue;
        } 
        set<long long> x;
        for(int i = 0, j = 0; i < s; ++i, j = (j + c) % k) {
            long long num = f(k, c, j);
            x.insert(num);
        }
        for(long long num : x) {
            cout << 1 + num << " ";
        }
        cout << "\n";
        x.clear();
    }
}
