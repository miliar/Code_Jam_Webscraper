#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

long long doit(long long n, long long p) {
    long long r = 2;
    long long ans = 0;
    n--;
    while (n >= 0 && p > (1LL << n)) {
        p -= 1LL << n;
        n--;
        r *= 2;
        ans = r - 2;
    }
    return ans;
}

long long doit2(long long n, long long p) {
    long long ans = 0;
    long long nn = n, pp = p;
    long long low = 0, high = (1LL << n);
    while(low + 1 < high) {
        long long mid = (low + high) / 2;
        long long down = (1LL << nn) - mid - 1;
        n = nn, p = pp;
        n--;
        p--;
        //cerr << mid << endl;
        long long m = (1LL << nn) - 1;
        while(n >= 0) {
            if (down == 0) {
                break;
            }
            down--;
            down /= 2;
            m ^= (1LL << n);
            n--;
        }
        //cerr << "  " << m << endl;
        if (m <= p) {
            low = mid;
        } else {
            high = mid;
        }
    }
    return low;
}

void solve() {
    long long n,p;
    cin >> n >> p;
    cout << min(doit(n,p), (1LL << n) - 1) << " " << doit2(n,p) << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i,T) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
