#include <iostream>

using namespace std;

const int maxn = 10000;

int cnt[25000];

void solve() {
    int n = 0;
    cin >> n;
    for (int j = 0; j < 25000; j++)
        cnt[j] = 0;
    for (int i = 0; i < n + n - 1; i++) {
        for (int j = 0; j < n; j++) {
            int x = 0;
            cin >> x;
            cnt[x] ^= 1;
        }
    }
    for (int i = 0; i < 25000; i++)
        if (cnt[i] == 1)
            cout << i << " ";
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test = 0;
    cin >> test;
    for (int id = 1; id <= test; id++) {
        cout << "Case #" << id << ": ";
        solve();
        cout << endl;
    }
    return 0;
}