#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int kases; cin >> kases;
    for (int kase=1; kase<=kases; kase++) {
        cout << "Case #" << kase << ": ";
        int N, R, P, S;
        cin >> N >> R >> P >> S;
        int r = 1, p = 0, s = 0;
        for (int i=0; i<N; i++) {
            int r_ = r + p;
            int p_ = p + s;
            int s_ = s + r;
            r = r_;
            p = p_;
            s = s_;
        }
        int cycles = 0;
        // might have to swap some stuff
        if (R != r || P != p || S != s) {
            swap(p, r);
            swap(r, s);
            cycles++;
        }
        if (R != r || P != p || S != s) {
            swap(p, r);
            swap(r, s);
            cycles++;
        }
        if (R != r || P != p || S != s) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        string RS = "R", PS = "P", SS = "S";
        for (int i=0; i<N; i++) {
            string RS_, PS_, SS_;
            // rock
            if (RS < SS) RS_ = RS + SS;
            else RS_ = SS + RS;
            // paper
            if (PS < RS) PS_ = PS + RS;
            else PS_ = RS + PS;
            // scissors
            if (SS < PS) SS_ = SS + PS;
            else SS_ = PS + SS;

            RS = RS_;
            PS = PS_;
            SS = SS_;
        }
        if (cycles == 0) {
            cout << RS << '\n';
        } else if (cycles == 1) {
            cout << PS << '\n';
        } else {
            cout << SS << '\n';
        }
    }
    return 0;
}
