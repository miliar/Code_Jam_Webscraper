#include <iostream>

using namespace std;

bool seen_all(bool seen[10]) {
    for (int i = 0; i < 10; i++) {
        if (!seen[i]) {
            return false;
        }
    }
    return true;
}

void add_to_seen(int N, bool seen[10]) {
    while (N > 0) {
        seen[N % 10] = true;
        N /= 10;
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";

        int N;
        cin >> N;
        if (N == 0) {
            cout << "INSOMNIA\n";
            continue;
        }

        int cur = 0;
        bool seen[10] = {false};
        while (!seen_all(seen)) {
            cur += N;
            add_to_seen(cur, seen);
        }
        cout << cur << "\n";
    }
}
