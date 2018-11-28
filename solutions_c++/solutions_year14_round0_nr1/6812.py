#include <bits/stdc++.h>
using namespace std;
int n, T;
int ans, x;
int used[200][20];
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int ans;
        cin >> ans;
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &x);
                if (i == ans) {
                    used[testcase][x]++;
                }
            }
        }
        cin >> ans;
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &x);
                if (i == ans) {
                    used[testcase][x]++;
                }
            }
        }
        int q = 0;
        for (int i = 1; i <= 16; i++) {
            if (used[testcase][i] == 2) {
               q++;
               ans = i;
            }
        }
        cout << "Case #" << testcase << ": ";
        if (q == 0) {
                cout << "Volunteer cheated!\n";
        } else if (q == 1) {
            cout << ans << endl;
        } else {
            cout << "Bad magician!\n";
        }
    }
    return 0;
}
