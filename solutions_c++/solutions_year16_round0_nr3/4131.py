#include <bits/stdc++.h>

using namespace std;

long long to_base(int x, int b) {
    long long ret = 0, pw = 1;
    while(x) {
        if(x & 1)
            ret += pw;
        x >>= 1;
        pw *= b;
    }
    return ret;
}

long long div(long long x) {
    for(long long d = 2; d * d <= x; ++d)
        if(x % d == 0)
            return d;
    return x;
}

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);

    int t, n, j;
    cin >> t;

    for(int tt = 1; tt <= t; ++tt) {
        cin >> n >> j;

        cout << "Case #" << tt << ":\n";

        int sols = 0;
        for(int i = (1 << (n - 1)) + 1; ; i += 2) {
            bool flag = 0;

            for(int b = 2; b <= 10; ++b) {
                long long no = to_base(i, b);
                if(div(no) == no)
                    flag = 1;
            }

            if(flag == 0) {
                for(int t = n - 1; t >= 0; --t)
                    cout << ((i >> t) & 1);
                cout << " ";
                for(int b = 2; b <= 10; ++b)
                    cout << div(to_base(i, b)) << " ";
                cout << '\n';
                sols += 1;
            }

            if(sols == j) break;
        }


        cout << endl;
    }
    return 0;
}
