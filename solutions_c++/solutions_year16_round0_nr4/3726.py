#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    long long T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        int K,C,S;
        cin >> K >> C >> S;
        assert(K == S);
        cout << "Case #" << t << ": ";
        for (int i=1; i<=K; ++i)
            (i == K) ? cout << i << endl : cout << i << " ";
    }
    return 0;
}

