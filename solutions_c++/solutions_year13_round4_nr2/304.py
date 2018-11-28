#include <iostream>
#include <algorithm>

using namespace std;

void solve()
{
    long long n, p;
    cin >> n >> p;
    if ((1ll << n) == p) {
        cout << p - 1 << " " << p - 1;
        return;
    }
    long long w_cnt = 0;
    while ((1ll << (n - w_cnt)) > p) ++w_cnt;
    long long l_cnt = 0;
    while ((1ll << (n - l_cnt)) > ((1ll << n) - p)) ++l_cnt;
    long long ll = (1ll << l_cnt) - 1;
    long long fw = (1ll << n) - (1ll << w_cnt);
    cout << max(ll - 1, 0ll) << " " << fw;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
