
#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i = 0; i < int(n); i++)
#define rep1(i,n) for (int i = 1; i <= int(n); i++)
#define var(x) #x " = " << x
#define show(x) cout << var(x) << endl;
#define all(c) (c).begin(), (c).end()
#define fst first
#define snd second
#define pb push_back

int main() {
    int T;
    cin >> T;
    rep1 (t,T) {
        cout << "Case #" << t << ": ";
        int K, C, S;
        cin >> K >> C >> S;
        // K == S
        cout << 1;
        for (int i = 2; i <= K; i++) cout << " " << i;
        cout << endl;
    }
}
