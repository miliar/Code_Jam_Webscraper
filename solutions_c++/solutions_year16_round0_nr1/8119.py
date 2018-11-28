#include <iostream>
#include <string>
using namespace std;

int add(int old, int n) {
    for (; n>0; n/=10) {
        int x = n%10;
        old |= (1<<x);
    }
    return old;
}

bool ok(int n) {
    return n == 1023;
}

int solve(int N) {
    int digits = 0;
    for (int i=1; i<1000006; ++i) {
        digits = add(digits, i*N);
        if (ok(digits)) return i*N;
    }
    return -1;
}

int main() {
    int T; cin >> T;
    for (int i=1; i<=T; ++i) {
        int N; cin >> N;
        int ans = solve(N);
        cout << "Case #" << i << ": ";
        if (ans <= 0)
            cout << "INSOMNIA" << endl;
        else cout << ans << endl;
    }
    return 0;
}
