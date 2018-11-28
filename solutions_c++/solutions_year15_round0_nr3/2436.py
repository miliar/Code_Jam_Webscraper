#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define PB push_back
#define MP make_pair
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define DEP(X,R,L) for(int X=R;X>=L;X--)
#define CLR(A,X) memset(A,X,sizeof(A))
#define IT iterator
#define X first
#define Y second
#define lson l,m,o<<1
#define rson m+1,r,o<<1|1
using namespace std;
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;
const int MAXN = 40010;
string s;
int l, x;
int frt[MAXN];

inline int id(char x) {
    if (x == 'i') return 2;
    if (x == 'j') return 3;
    return 4;
}

int m[5][5] = {0, 0, 0, 0, 0,
               0, 1, 2, 3, 4,
               0, 2, -1, 4, -3,
               0, 3, -4, -1, 2,
               0, 4, 3, -2, -1};

void init() {
    string t = s + s + s + s;
    int len = t.length();
    REP(i, len) {
        if (i == 0) frt[0] = id(t[0]);
        else {
            if (frt[i-1] < 0) frt[i] = -m[-frt[i-1]][id(t[i])];
            else frt[i] = m[frt[i-1]][id(t[i])];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("C-small-attempt3.out", "w", stdout);
    int t, cas = 1;
    cin >> t;
    while (t--) {
        cout << "Case #" << cas++ << ": ";
        cin >> l >> x;
        cin >> s;
        string tmp = s;
        int lens = s.length();
        init();
        REP(i, x-1) {
            s += tmp;
        }
        int len = s.length();
        if (frt[(len-1)%(4*lens)] != -1) {
            cout << "NO" << endl;
            continue;
        }
        bool flag1 = false, flag2 = false;
        REP(i, len) {
            if (frt[i%(4*lens)] == 2 && i < len-2) {
                flag1 = true;
            }
            if (frt[i%(4*lens)] == 4 && flag1 && i < len-1) {
                flag2 = true;
                break;
            }
        }
        if (flag1 && flag2) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}

