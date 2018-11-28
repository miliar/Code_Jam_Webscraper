#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

void solve(){
    int k, c, s;
    cin >> k >> c >> s;
    long long add = 1;
    for (int i = 1; i < c; i++) add *= k;
    long long cur = 1;
    for (int i = 0; i < k; i++)
        cout << cur << " ", cur += add;
    cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}
