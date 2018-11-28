#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)

using namespace std;

void print_binary(long long X) {
    string str;
    while (X > 0) {
        str +='0' + (X % 2);
        X /= 2;
    }
    reverse(str.begin(), str.end());
    cout << str;
}

int magic[9] = {3, 7, 5, 6, 31, 8, 27, 5, 77};

void solve() {
    int N, J;
    cin >> N >> J;

    cout << endl;
    rep(i, J) {
        long long X = (1LL << 15) + 1;
        int tmp = i;
        rep(j, 100) {
            if (tmp == 0) break;
            if (tmp % 2) {
                X |= 9 << (j + 1 + (j / 3) * 3);
            }
            tmp /= 2;
        }

        print_binary(X);
        rep(j, 9) {
            cout << " " << magic[j];
        }
        cout << endl;
    }
}

int main() {
    int N;
    cin >> N;
    rep(i, N) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
