#include <cstdio>
#include <iostream>

using namespace std;

#define INF 0x3f3f3f3f

string s;
int D[100][2];

int solve() {
    int N = s.size();

    D[0][0] = 0;
    D[0][1] = 0;
    for (int i = 0; i < N; i++) {
        D[i + 1][0] = INF;
        D[i + 1][1] = INF;

        int seq_side = (s[i] == '+') ? 0 : 1;
        for (int j = i; j >= 0; j--) {
            int p_side = (s[j] == '+') ? 0 : 1;
            if (p_side != seq_side) {
                break;
            }
 
            int swap_cnt = (j == 0) ? 1 : 3;
            if (seq_side == 0) {
                D[i + 1][0] = min(D[i + 1][0], D[j][0]);
                D[i + 1][1] = min(D[i + 1][1], D[j][1] + swap_cnt);
            } else {
                D[i + 1][0] = min(D[i + 1][0], D[j][0] + swap_cnt);
                D[i + 1][1] = min(D[i + 1][1], D[j][1]); 
            }
        }

        D[i + 1][0] = min(D[i + 1][0], D[i + 1][1] + 1);
        D[i + 1][1] = min(D[i + 1][1], D[i + 1][0] + 1);
    }

    /*for (int i = 0; i < N; i++) {
        cout << D[i + 1][0];
    }
    cout << endl;
    for (int i = 0; i < N; i++) {
        cout << D[i + 1][1];
    }
    cout << endl;*/


    return D[N][0];
}

int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> s;
        // cout << s << endl;
        int ans = solve();
        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}
