#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
template <class T> int size(const T &x) { return x.size(); }
const int INF = 2147483647;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

string get(int n, char win) {
    if (n == 0) {
        return string("") + win;
    } else if (win == 'P') {
        string a = get(n-1, 'P'),
               b = get(n-1, 'R');
        return min(a,b) + max(a,b);
    } else if (win == 'R') {
        string a = get(n-1, 'R'),
               b = get(n-1, 'S');
        return min(a,b) + max(a,b);
    } else {
        assert(win == 'S');
        string a = get(n-1, 'S'),
               b = get(n-1, 'P');
        return min(a,b) + max(a,b);
    }
}

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        cout << "Case #" << (t+1) << ": ";
        int n,r,p,s;
        cin >> n >> r >> p >> s;
        vector<string> poss;
        poss.push_back(get(n,'P'));
        poss.push_back(get(n,'R'));
        poss.push_back(get(n,'S'));
        sort(poss.begin(), poss.end());
        bool found = false;
        rep(i,0,size(poss)) {
            int a = 0,
                b = 0,
                c = 0;
            rep(j,0,size(poss[i])) {
                char cur = poss[i][j];
                if (cur == 'P') a++;
                else if (cur == 'R') b++;
                else {
                    assert(cur == 'S');
                    c++;
                }
            }
            if (a == p && b == r && c == s) {
                cout << poss[i] << endl;
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

