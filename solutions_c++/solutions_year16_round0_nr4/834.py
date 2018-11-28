#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;


int main() {
    #ifdef LOCAL
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    #endif    	   	

    int T;
    cin >> T;
    for (int __it = 1; __it <= T; ++__it) {
        int K, C, S;
        cin >> K >> C >> S;
    	cout << "Case #" << __it << ":";

        int sC = (K + C - 1) / C;
        if (sC > S) {
            cout << " IMPOSSIBLE\n";
            continue;
        }

        vector<ll> pK(C + 1);
        pK[0] = 1;
        for (int i = 1; i <= C; ++i) {
            pK[i] = pK[i - 1] * K;
        }

        int posi = 0;
        for (int i = 0; i < sC; ++i) {
            ll pos = 0;

            for (int j = 0; j < C; ++j) {
                pos += posi * pK[j];

                if (++posi == K) {
                    posi = 0;
                }
            }

            cout << " " << (pos + 1);
        }
        cout << "\n";
    }


    return 0;
}
