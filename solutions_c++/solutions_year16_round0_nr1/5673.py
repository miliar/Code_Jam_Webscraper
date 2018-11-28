#include <bits/stdc++.h>

using namespace std;

void solve(int test) {

    long long n;
    cin >> n;
    printf("Case #%d: ", test);
    if (n == 0) {
        cout << "INSOMNIA" << "\n";
        return ;
    }
    long long cur = n;
    set<int> used;
    while (true) {
        long long x = cur;
        while (x > 0) {
            used.insert(x % 10);
            x /= 10;
        }
        if (used.size() == 10) {
            break;
        }
        cur += n;
    }
    cout << cur << "\n";
    if (test % 1000 == 0) {
        cerr << test << endl;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int test;
    cin >> test;
    //test = 1E6;
    for (int i = 1; i <= test; i++) {
        solve(i);
    }
    return 0;
}
