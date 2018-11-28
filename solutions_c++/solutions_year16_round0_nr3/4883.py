#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(void) {
    int T, cas = 1;
    cin >> T;
    while (T -- > 0) {
        int N, J;
        cin >> N >> J;
        cout << "Case #" << (cas ++) << ":\n";
        for (int i = 1; i < (1<<N) && J > 0; ++ i) {
            int n = i;
            if (n % 2 == 0) continue;
            if ((n & (1<<(N-1))) == 0) continue;
            for (int j = 2; j <= 10; ++ j) {
                ll m = 0;
                for (int k = N-1; k >= 0; -- k) {
                    if (n & (1<<k)) m = m * j + 1;
                    else m = m * j;
                }
            }
        }
    }

    return 0;
}
