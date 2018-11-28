#include <iostream>
#include <string>
#include <vector>

using namespace std;
using ll = long long;

int main()
{
    int T; cin >> T;
    for (int cas = 1; cas <= T; ++cas) {
        int K, C, S; cin >> K >> C >> S;
        vector<ll> expo(C);
        ll ex = 1;
        for (int i = C-1; i >= 0; --i) {
            expo[i] = ex;
            ex *= K;
        }

        if (K == S) { // small input
            vector<ll> check(S);
            for (int k = 0; k < K; ++k) {
                for (int depth = 0; depth < C; ++depth) {
                    check[k] += expo[depth] * k;
                }
            }

            cout << "Case #" << cas << ":";
            for (auto s: check)
                cout << " " << s+1;
            cout << "\n";
        }
    }

    return 0;
}
