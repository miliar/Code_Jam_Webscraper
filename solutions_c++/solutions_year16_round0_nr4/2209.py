#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (int)n; ++i)
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
void solve() {
    ll K, C, S;
    cin >> K >> C >> S;
    ll ptr = 1;
    FOR(i, C - 1) {
        ptr *= K;
    }
    assert(S == K);
    ll cur = ptr;
    FOR(i, S) {
        printf(" %lld", cur);
        cur += ptr;
    }
    printf("\n");
    return;
}
int main() {
    int TestCase;
    cin >> TestCase;
    FOR(caseID, TestCase) {
        cout << "Case #" << caseID + 1 << ":";
        solve();
    }
    return 0;
}
