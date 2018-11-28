#include <iostream>

using namespace std;

typedef long long ll;

inline void update_mask(ll& mask, ll N) {
    while(N > 0) {
        ll r = N % 10;
        N /= 10;
        mask |= (1<<r);
    }
}

void solve(ll N) {

    if(N == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }

    ll mask = 0;
    ll all_mask = 1023;

    ll n = N;
    update_mask(mask, n);

    while(mask != all_mask) {
        n += N;
        update_mask(mask, n);
    }

    cout << n << endl;
}

int main() {

    int T;
    cin >> T;
    int c = 1;
    while(T --> 0) {
        int N;
        cin >> N;
        cout << "Case #" << c++ << ": ";
        solve(N);
    }

    return 0;
}