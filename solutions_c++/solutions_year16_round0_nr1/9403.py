#include <iostream>
#include <cstdint>

using namespace std;

int solve(int64_t n) {
    bool seen[10] = {false};

    int64_t curr = n;
    for (;;) {
        if (curr == 0) {
            return -1;
        }

        int64_t check = curr;
        while (check > 0) {
            int digit = check % 10;
            check /= 10;
            seen[digit] = true;
        }

        bool seen_all = true;
        for (int i = 0; (i < 10) && seen_all; ++i) {
            seen_all = seen_all && seen[i];
        }

        if (seen_all) {
            return curr;
        }

        curr += n;
    }

    return -1;
}

int main() {
    int tn; cin >> tn;
    for (int tc = 1; tc <= tn; ++tc) {
        int64_t n; cin >> n;
        int res = solve(n);
        cout << "Case #" << tc << ": ";
        if (res < 0) {
            cout << "INSOMNIA\n";
        } else {
            cout << res << "\n";
        }
    }
    return 0;
}
