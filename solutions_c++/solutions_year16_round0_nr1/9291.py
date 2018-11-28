#include<bits/stdtr1c++.h>
using namespace std;

typedef long long ll;

ll T, N;
bool vis[10];

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        cin >> N;
        if (N == 0) cout << "INSOMNIA\n";
        else {
            memset(vis, 0, sizeof vis);
            ll i;
            for (i = 1LL; i < 1000000; ++i) {
                ll p = i * N;
                while (p != 0) {
                    vis[p%10] = true;
                    p/=10;
                }
                bool good = true;
                for (int i = 0; i < 10; ++i)
                    good &= vis[i];
                if (good) break;
            }
            cout << i*N << "\n";
        }
    }
    
    return 0;
}
