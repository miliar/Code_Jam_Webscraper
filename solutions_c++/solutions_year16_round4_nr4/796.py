#include <bits/stdc++.h>
using namespace std;

int n;

int worker[4];
bool mfree[4];
int state;
int input;

bool canwork(int id, int mach) {
    return (state & (1 << (id * n + mach))) != 0;
}

bool hassol(int day) {
    if (day == n)
        return true;
    bool ok = false;
    for (int m = 0; m < n; ++m) {
        if (mfree[m] && canwork(worker[day], m)) {
            ok = true;
        }
    }

    for (int m = 0; m < n; ++m) {
        if (mfree[m] && canwork(worker[day], m)) {
            mfree[m] = false;
            ok = ok && hassol(day + 1);
            mfree[m] = true;
        }
    }
    return ok;
}

void solveprob2() {
    int best = 99999;
    for (int sol = 0; sol < (1 << (n * n)); ++sol) {
        state = sol;
        if ((state & input) != input)
            continue;
        // cout << "testing " << sol << "from " << input << endl;
        for (int i = 0; i < n; ++i) {
            worker[i] = i;
            mfree[i] = 1;
        }

        bool ok = true;
        do {
            ok = ok && hassol(0);
        } while (next_permutation(worker, worker + n));
        if (ok) {
            // cout << state << endl;
            int value = __builtin_popcount(state - input);
            best = min(best, value);
        }
    }
    cout << best << endl;
}

int main() {
    int ts;
    cin >> ts;
    for (int t = 1; t <= ts; ++t) {
        cin >> n;
        input = 0;
        for (int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            for (int j = 0; j < n; ++j) {
                if (s[j] == '1') {
                    int id = i;
                    int mach = j;
                    input |= (1 << (id * n + mach));
                }
            }
        }
        cout << "Case #" << t << ": ";
        solveprob2();
    }
}
