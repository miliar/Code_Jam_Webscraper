#include <bits/stdc++.h>
using namespace std;

int T;

template <class TMP> void print(int i, TMP x) {
        cout << "Case #" << i << ": " << x << endl;
}

int main() {
    cin >> T;
    for(int tt = 1; tt <= T; ++tt) {
        int c, k, s;
        cin >> k >> c >> s;
        cout << "Case #" << tt << ": ";
        if(k != s) cerr << "DO NOT SUBMIT!!!" << endl;
        for(int i = 0; i < k; ++i) {
            long long an = i + 1;
            long long bi = 1;
            for(int j = 0; j < c-1; ++j) {
                bi *= k;
                for(int h = 0; h < i; ++h) {
                    an += bi;
                }
            }
            cout << an;
            if(i != k-1) cout << " ";
        }
        cout << endl;
    }

    return 0;
}
