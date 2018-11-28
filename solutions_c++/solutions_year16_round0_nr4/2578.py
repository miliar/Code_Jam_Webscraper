#include <bits/stdc++.h>

#define debug(x) cout << "> " << #x << " = " << x << endl;
#define debugat(arr, at) cout << "> " << #arr << "[" << at << "] = " << arr[at] << endl;

using namespace std;

typedef long long ll;

int main() {

    int tests;
    scanf("%d", &tests);
    
    for(int t = 1; t <= tests; ++t) {
        ll k, c, s;
        scanf("%lld %lld %lld", &k, &c, &s);
        printf("Case #%d:", t);
        if(s < k) {
            printf("IMPOSSIBLE\n");
        }
        else {
            ll next = 1LL;
            for(ll i = 1; i < c; ++i)
                next *= k;
            for(ll i = 1; i <= k; ++i) {
                cout << " " << i * next;
            }
            cout << "\n";
        }
    }
    return 0;
}
