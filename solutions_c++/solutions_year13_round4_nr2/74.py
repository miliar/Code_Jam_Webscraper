#include <iostream>
using namespace std;

long long solve(int N, long long P) {
    if (P == (1LL<<N)) return (1LL<<N)-1;
    if (P == 0) return -1;

    bool bits[N];
    for (int i = 0; i < N; i++) {
        bits[N-1-i] = P%2;
        P = P/2;
    }
    long long needed = 2;
    for (int i = 0; i < N; i++) {
        if (!bits[i]) needed *= 2;
        else break;
    }
    return (1LL<<N)-needed;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        long long P;
        cin >> N >> P;
        cout << "Case #" << t << ": " << ((1LL<<N)-2-solve(N, (1LL<<N)-P)) << ' ' << solve(N, P) << '\n';
    }
    return 0;
}
