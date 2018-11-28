#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool check(bool *used)
{
    for (int i = 0; i < 10; i++) {
        if (!used[i]) {
            return 0;
        }
    }
    return 1;
}

int main()
{
    ll T, N;
    cin >> T;
    for (int tc = 0; tc < T; tc++) {
        cin >> N;
        cout << "Case #" << tc+1 << ": ";
        if (N == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        bool used[10] = {0};
        ll j = -1;
        for (ll i = 1; i < 114514; i++) {
            ll k = N*i;
            while (k > 0) {
                used[k%10] = 1;
                k /= 10;
            }
            if (check(used)) {
                j = i;
                break;
            }            
        }
        if (j != -1) {
            cout << N*j << endl;
        } else {
            cout << "INSOMNIA" << endl;
        }
    }
    return 0;
}
