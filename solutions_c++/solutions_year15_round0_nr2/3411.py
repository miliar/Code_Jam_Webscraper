#include <iostream>

using namespace std;

void solve(const int test) {
    int n; cin >> n;
    static int s[1010]; for (int i=0; i<n; ++i) cin >> s[i];
    int ans = 0x7f7f7f7f;
    for (int limit = 1; limit <= 1000; ++limit) {
        int curans = limit;
        for (int i=0; i<n; ++i)
            curans += (s[i] + limit - 1) / limit - 1;
        ans = min(ans, curans);
    }

    cout << "Case #" << test << ": " << ans << endl;
}

int main() {
    int t; cin >> t;
    for (int e=0; e<t; ++e)
        solve(e+1);

    return 0;
}

