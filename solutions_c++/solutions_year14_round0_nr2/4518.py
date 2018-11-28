#include <bits/stdc++.h>

using namespace std;

int main() {
    //freopen("in.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int casos;
    cin >> casos;
    cout.precision(10);
    for(int caso = 1 ; caso <= casos ; caso++){
        double C,F,X;
        cin >> C >> F >> X;
        double r = 2.0, ans = X/r, currt = 0.0, t;
        for(int f = 1 ; f <= 100000 ; f++){
            currt += C/r;
            r += F;
            t = X/r + currt;
            ans = min(ans,t);
        }
        cout << "Case #" << caso << ": " << fixed << ans << endl;
    }
}
