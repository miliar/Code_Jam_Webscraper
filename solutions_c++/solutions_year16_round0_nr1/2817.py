#include <bits/stdc++.h>
using namespace std;

int T;

template <class T> void print(int i, T x) {
    cout << "Case #" << i << ": " << x << endl;
}

int main() {
    cin >> T;
    for(int tt = 1; tt <= T; ++tt) {
        long long n;
        cin >> n;
        if(n == 0) {
            print(tt, "INSOMNIA");
            continue;
        }
        long long number[10];
        long long digit = 10;
        long long ans = n;
        fill(number, number + 10, 0);
        for(int k = 1; ; ++k) {
            ans = n * k;
            long long z = ans;
            while(z) {
                int dig = z % 10;
                number[dig]++;
                z = z / 10;
            }
            int d = 0;
            for(int i = 0; i < 10; ++i) {
                if(number[i]) {
                    ++d;
                }
            }
            if(d == 10) {
                break;
            }       
        }
        print(tt, ans);
    }
    return 0;
}
