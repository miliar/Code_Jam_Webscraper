#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

#define fr(a, b, c) for(int a = b; a < c; a++)

typedef long long ll;

ll k, c, s;

int main() {
    ios_base::sync_with_stdio(false);

    int T;

    cin >> T;

    fr(cas, 1, T+1) {
        cin >> k >> c >> s;

        if((k + c - 1)/c > s) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }

        vector<ll> ans;

        ll first = 1;

        fr(i, 1, c) first *= k;

        for(int i = 0; i < k; i += c) {
            ll b = first;
            ll n = 0;
            for(int j = 0; j < c && i + j < k; j++) {
                n += (i + j) * b;
                b /= k;
            }

            ans.push_back(n);
        }

        printf("Case #%d:", cas);

        fr(i, 0, ans.size()) {
            printf(" %lld", ans[i] + 1);
        }

        puts("");
    }

    return 0;
}