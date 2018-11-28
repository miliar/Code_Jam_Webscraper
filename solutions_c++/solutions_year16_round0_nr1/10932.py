#include <bits/stdc++.h>
#define INF 2e9
#define pb push_back
#define mp make_pair
#define forn(i,n) for (int i = 0; i < n; i++)

using namespace std;

typedef long long ll; 

int cnt[10];

void update(ll x) {
    while (x) {
        cnt[x % 10]++;
        x /= 10;
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int tests;
    cin >> tests;

    for (int it = 0; it < tests; it++) {

        cout << "Case #" << it + 1 << ": ";

        forn (i, 10) {
            cnt[i] = 0;
        }

        int n;
        cin >> n;

        if (n == 0) {
            cout << "INSOMNIA" << endl;    
            continue;
        }

        ll k = n;
        while (true) {
           update(k);
           bool flag = true;
           forn (i, 10) {
               if (!cnt[i]) {
                   flag = false;
               }
           }
           if (flag) {
               cout << k << endl;
               break;
           } else {
               k += n;
           }
        }
    }

    return 0;
}
