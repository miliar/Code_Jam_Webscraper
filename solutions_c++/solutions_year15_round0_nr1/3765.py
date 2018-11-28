#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

void solve() {
    int N;
    cin >> N;
    string counts;
    cin >> counts;
    assert(counts.size() == N+1);
    int sum = 0;
    int ans = 0;
    for (int i = 0; i < counts.size(); ++i) {
        const int cur = counts[i] - '0'; 
        ans = max(i - sum, ans);
        sum += cur;
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
}
