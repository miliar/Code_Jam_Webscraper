#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;


int main() {
    int t;
    cin >> t;
    int cas = 1;
    while (t--) {
        cout << "Case #" << cas << ":" << endl;
        cas++;
        int n, j;
        cin >> n >> j;
        for (int i = 0; i < j; ++i) {
            cout << 1;
            int x = i;
            for (int j = 0; j < (n - 2)/2; ++j) {
                if (x%2) cout << "11";
                else cout << "00";
                x /= 2;
            }
            cout << 1;
            for (int j = 3;  j <= 11; ++j) cout << ' ' << j;
            cout << endl;
        }
    }
}