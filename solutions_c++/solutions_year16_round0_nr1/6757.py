#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        int N; cin >> N;
        set<int> s;
        int ans = 1 << 28;
        for (int i = 0; i < 100; i++) {
            int tmp = (i + 1) * N;
            while (tmp) {
                s.insert(tmp % 10);
                tmp /= 10;
            }

            if (s.size() >= 10) {
                ans = (i + 1) * N;
                break;
            }
        }

        cout << "Case #" << t + 1 << ": ";
        if (ans < (1 << 28)) cout << ans << endl;
        else cout << "INSOMNIA" << endl;

    }

    return 0;
}
