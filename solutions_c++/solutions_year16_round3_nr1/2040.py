#include <iostream>
#include <string>
using namespace std;

const string alphabeta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int ct[26];
int mx1, mx2;

int max12() {
    int total = 0;
    mx1 = mx2 = -1;
    for (int i=0; i<26; ++i) if (ct[i]>0) {
        total += ct[i];
        if (mx1==-1 || ct[i] >= ct[mx1]) {
            mx2 = mx1;
            mx1 = i;
        } else if (mx2==-1 || ct[i]> ct[mx2]) {
            mx2 = i;
        }
    }
    return total;
}

void solve() {
    while (true) {
        int total = max12();
        if (total == 0) break;
        if (ct[mx1] > ct[mx2]) {
            cout << " " << alphabeta[mx1] << alphabeta[mx1];
            ct[mx1] -= 2;
        } else if (ct[mx1]==1 && total==3) {
            cout << " " << alphabeta[mx1];
            ct[mx1] -= 1;
        } else {
            cout << " " << alphabeta[mx1] << alphabeta[mx2];
            ct[mx1] -= 1;
            ct[mx2] -= 1;
        }
    }
}

int main() {
    int T; cin >> T;
    for (int i=1; i<=T; ++i) {
        int N; cin >> N;
        memset(ct, 0, sizeof(ct));
        for (int j=0; j<N; ++j)
            cin >> ct[j];
        cout << "Case #" << i << ":";
        solve();
        cout << endl;
    }
    return 0;
}
