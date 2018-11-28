#include <bits/stdc++.h>

using namespace std;

void solve(){
    long long n;
    cin >> n;
    if (n == 0) {
        cout << "INSOMNIA\n";
        return;
    }
    set <int> tmp;
    tmp.clear();
    for (int i = 0; i <= 9; i++)
        tmp.insert(i);
    for (long long i = n; ; i += n) {
        long long x = i;
        while (x > 0) {
            tmp.erase(x % 10);
            x /= 10;
        }
        if (tmp.size() == 0)
        {
            cout << i << endl;
            return;
        }
    }
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test = 0;
    cin >> test;
    for (int id = 1; id <= test; id++){
        cout << "Case #" << id << ": ";
        solve();
    }
    return 0;
}