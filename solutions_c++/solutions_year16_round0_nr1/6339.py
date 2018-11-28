#include <bits/stdc++.h>

#define all(v) (v).begin(), (v).end()

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

bool used[10];

bool ok() {
    for(int i = 0; i < 10; i++) if(!used[i]) return false;
    return true;
}

bool calc(ll x) {
    for(ll i = 10; x != 0; x /= i) {
        used[(int)(x % i)] = true;
    }
}

int main() {
    int T;
    ll N;
    while(cin >> T) {
        for(int i = 1; i <= T; i++) {
            memset(used, 0, sizeof used);
            cin >> N;

            if(N == 0LL) {
                printf("Case #%d: %s\n", i, "INSOMNIA");
                continue;
            }

            for(ll x = 1; ; x++) {
                calc(x * N);
                if(ok()) {
                    printf("Case #%d: %lld\n", i, x*N);
                    break;
                }
            }
        }
    }
}

