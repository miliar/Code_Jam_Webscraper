#include <cstdio>
#include <iostream>

using namespace std;

int P[1010], N, who1, who2, M;

bool checkOne(int who) {
    if (P[who] == 0) return false;
    for (int i = 1; i <= N; ++i) {
        if (who == i) {
            if ((P[i] - 1) > ((M - 1) / 2)) {
                return false;
            }
        } else {
            if ((P[i]) > ((M - 1) / 2)) {
                return false;
            }
        }
    }
    return true;
}

int evacuationOne() {
    for (int i = 1; i <= N; ++i) {
        if (checkOne(i)) {
            return i;
        }
    }
    return -1;
}

bool checkTwo(int who1, int who2) {
    if (P[who1] == 0 || P[who2] == 0) return false;
    for (int i = 1; i <= N; ++i) {
        if (who1 == i || who2 == i) {
            if ((P[i] - 1) > ((M - 2) / 2)) {
                return false;
            }
        } else {
            if ((P[i]) > ((M - 2) / 2)) {
                return false;
            }
        }
    }
    return true;
}

void evacuationTwo() {
    for (int i = 1; i <= N; ++i) {
            for (int j = i + 1; j <= N; ++j) {
                if (checkTwo(i, j)) {
                    who1 = i;
                    who2 = j;
                    return;
                }
            }
    }
}

void solve() {
    while (1) {
        if (M == 0)
            break;

        int who = evacuationOne();
        if (who != -1) {
            P[who] -= 1;
            cout << " " << char(who + (int)'A' - 1);
            M -= 1;
        } else {
            evacuationTwo();
            P[who1] -= 1;
            P[who2] -= 1;
            cout << " " << char(who1 + (int)'A' - 1) << char(who2 + (int)'A' - 1);
            M -= 2;
        }
    }


}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;

    cin >> T;

    for (int i = 1; i <= T; ++i) {
        cin >> N;
        M = 0;

        for (int j = 1; j <= N; ++j) {
                cin >> P[j];
                M += P[j];
        }

        cout << "Case #" << i << ":";
        solve();
        cout << endl;
    }

    return 0;
}
