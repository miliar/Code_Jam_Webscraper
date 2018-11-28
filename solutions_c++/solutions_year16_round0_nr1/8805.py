#include <bits/stdc++.h>

using namespace std;
long long T, N;

bool seen[10];
long long solve() {
    memset(seen, false, sizeof(seen));
    int ctr = 0;
    long long cur = 0;
    do {
        cur += N;
        string num = to_string(cur);
        for (char ch : num) {
            if (!seen[ch-'0']) {
                ctr++;
                seen[ch-'0'] = true;
            }
        }
    } while (ctr < 10);
    return cur;
}

int main() {
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        cin >> N;
        if (N == 0) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << solve() << endl;
        }


    }
    return 0;
}
