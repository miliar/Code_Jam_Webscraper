#include <bits/stdc++.h>

using namespace std;

bool digit[10];

void proc(int N) {
    if (N == 0) digit[0] = 1;
    else {
        while (N) {
            digit[N % 10] = 1;
            N /= 10;
        }
    }
}

bool ok() {
    for (int i = 0; i < 10; i++)
        if (!digit[i]) return 0;
    return 1;
}

void solve(int N) {
    if (N == 0) {
        cout << "INSOMNIA"; return;
    }
    int _N = N;
    proc(N);
    while (!ok()) {
        N += _N;
        proc(N);
    }
    cout << N;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    ios::sync_with_stdio(0);
    int T; cin >> T;
    for (int te = 1; te <= T; te++) {
        memset(digit, 0, sizeof digit);
        int N; cin >> N;
        cout << "Case #" << te << ": ";
        solve(N);
        cout << '\n';
    }
    
    return 0;
}
