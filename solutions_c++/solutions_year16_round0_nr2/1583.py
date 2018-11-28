
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

template <class T> void chmax(T& x, T const& y) { x = max(x,y); }
template <class T> void chmin(T& x, T const& y) { x = min(x,y); }

int main() {
    int T;
    cin >> T;
    rep1 (t,T) {
        string s;
        cin >> s;
        cout << "Case #" << t << ": ";

        s.erase(unique(all(s)), s.end());
        if (s[0] == '+') {
            cout << s.size()/2*2 << endl;
        } else {
            cout << (s.size()+1)/2*2 - 1 << endl;
        }
    }
}
