#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(void) {
    int T, cas = 1;
    cin >> T;
    while (T -- > 0) {
        int N;
        cin >> N;
        cout << "Case #" << (cas ++) << ": ";
        if (N == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }

        bool vis[10] = {false};
        int cnt = 0;
        ll M = N;
        while ( cnt < 10 ) {
            int x = M;
            while (x > 0) {
                if (!vis[x % 10]) {
                    ++ cnt;
                    vis[x % 10] = true;
                }
                x /= 10;
            }
            if (cnt >= 10) break;
            M += N;
        }
        cout << M << endl;
    }

    return 0;
}
