#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair <int, int> ii;
typedef vector <int> vi;
typedef double ld;
#define X first
#define Y second
#define mk make_pair
#define pb push_back
#define Rep(i, n) for(int i = 0; i < int(n); i ++)
const int MOD = (int) 1e9 + 7;
void MAIN();
int main(){
    //freopen("input.txt", "r", stdin);
    ios:: sync_with_stdio(false); cin.tie(0);
    MAIN();
    return 0;
}
////////////////////////////////////////////////////////////////////////

const int N = 16;

struct prs {
    int p, r, s;
    prs(int p, int r, int s):
        p(p), r(r), s(s) {}
    prs():
        p(0), r(0), s(0) {}

    prs operator + (const prs &x) {
        return prs(p + x.p, r + x.r, s + x.s);
    }

    bool operator == (const prs &x) {
        return p == x.p && r == x.r && s == x.s;
    }
};

prs p[N], r[N], s[N];
string a[N], b[N], c[N];

void MAIN(){
    int tc;
    cin >> tc;

    p[0] = prs(1, 0, 0);
    r[0] = prs(0, 1, 0);
    s[0] = prs(0, 0, 1);
    a[0] = "P";
    b[0] = "R";
    c[0] = "S";

    for (int i = 1; i <= 12; ++i) {
        p[i] = p[i-1] + r[i-1];
        r[i] = p[i-1] + s[i-1];
        s[i] = r[i-1] + s[i-1];
        a[i] = a[i-1] + b[i-1];
        b[i] = a[i-1] + c[i-1];
        c[i] = b[i-1] + c[i-1];
    }

    cout.precision(8);
    for (int cs = 1; cs <= tc; ++cs) {
        int n, P, R, S;
        cin >> n >> R >> P >> S;
        if (prs(P, R, S) == p[n]) {
            cout << "Case #" << cs << ": " << a[n] << endl;
            cerr << "Case #" << cs << ": " << a[n] << endl;
        } else if (prs(P, R, S) == r[n]) {
            cout << "Case #" << cs << ": " << b[n] << endl;
            cerr << "Case #" << cs << ": " << b[n] << endl;
        } else if (prs(P, R, S) == s[n]) {
            cout << "Case #" << cs << ": " << c[n] << endl;
            cerr << "Case #" << cs << ": " << c[n] << endl;
        } else {
            cout << "Case #" << cs << ": IMPOSSIBLE" << endl;
            cerr << "Case #" << cs << ": IMPOSSIBLE" << endl;
        }
    }
}
