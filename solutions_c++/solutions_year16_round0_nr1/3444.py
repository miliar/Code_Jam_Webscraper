#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define rep2(i,a,b) for (int i=(a);i<(b);i++)
#define rrep(i,n) for (int i=(n)-1;i>=0;i--)
#define rrep2(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define all(a) (a).begin(),(a).end()

typedef long long ll;
typedef pair<int, int> P;
typedef vector<int> vi;
typedef vector<P> vp;
typedef vector<ll> vll;

bool found[10];

void updateFoundDigits(ll x) {
    while (x > 0) {
        found[x % 10] = true;
        x /= 10;
    }
}

bool FoundAllDigits() {
    rep(i, 10) {
        if (!found[i]) return false;
    }
    return true;
}


signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        ll N;
        cin >> N;
        ll sum_N = N;
        bool solved = false;
        fill(found, found + 10, false);
        for (int j = 1; j <= 10000; j++) {
            updateFoundDigits(sum_N);
            if (FoundAllDigits()) {
                printf("Case #%d: %lld\n", i, sum_N);
                solved = true;
                break;
            }
            sum_N += N;
        }
        if (!solved) {
            printf("Case #%d: INSOMNIA\n", i);
        }
    }
}
