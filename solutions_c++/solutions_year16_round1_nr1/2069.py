# include <bits/stdc++.h>

using namespace std;

int main() {
    int t, I = 0;
    string p, r;
    cin >> t;

    while(t--) {
        cin >> p;
        r = p[0];
        for(int i = 1; i < p.size(); ++i) {
            if(r[0] <= p[i]) {
                r = p[i] + r;
            } else {
                r += p[i];
            }
        }
        cout << "Case #" << ++I << ": "<< r << endl;
    }
    return 0;
}
