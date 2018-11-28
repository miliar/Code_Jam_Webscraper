#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

void solve() {
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    string Rs = "R", Ps = "P", Ss = "S";
    while (N) {
        string As = (Rs < Ps ? Rs + Ps : Ps + Rs);
        string Bs = (Ss < Ps ? Ss + Ps : Ps + Ss);
        string Cs = (Ss < Rs ? Ss + Rs : Rs + Ss);
        int A = (R + P - S) / 2;
        int B = (P + S - R) / 2;
        int C = (R + S - P) / 2;
        if (A < 0 || B < 0 || C < 0) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        R -= A;
        P -= B;
        S -= C;
        Rs = Cs;
        Ps = As;
        Ss = Bs;
        N--;
    }
    cerr << R << " "  << P << " " << S << " " << endl;
    if (R) {
        cout << Rs << endl;
    } else if (P) {
        cout << Ps << endl;
    } else if (S) {
        cout << Ss << endl;
    } else {
        cout << "ERROR" << endl;
    }
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
