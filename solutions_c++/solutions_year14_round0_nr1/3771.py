#include <iostream>
#include <cstring>
using namespace std;

int cnt[20];

void calc() {
    int n, x;
    cin >> n;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> x;
            if (i == n - 1) cnt[x]++;
        }
    }
}

int main() {
    freopen("p1.in", "r", stdin);
    freopen("p1.out", "w", stdout);

    int T, Case = 1;
    cin >> T;
    while (T--) {
        memset(cnt, 0, sizeof(cnt));
        calc();
        calc();
        int ans = -1;
        int two = 0;
        for (int i = 1; i <= 16; i++) {
            if (cnt[i] == 2) {
                two++;
                ans = i;
            }
        }
        cout << "Case #" << Case++ << ": ";
        if (ans == -1) {
            cout << "Volunteer cheated!" << endl;
        } else if (two > 1) {
            cout << "Bad magician!" << endl;
        } else cout << ans << endl;
    }
    return 0;
}
