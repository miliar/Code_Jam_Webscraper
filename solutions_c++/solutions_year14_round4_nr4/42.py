
#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define fup FOR
#define fdo FORD
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define siz SZ
#define CLR(x) memset((x), 0, sizeof(x))
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define FI X
#define SE Y
#define SQR(a) ((a)*(a))
#define DEBUG 0
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> P;
typedef vector<int> VI;
const int INF=1E9+7;
template<class C> void mini(C&a4, C b4) { a4 = min(a4, b4); }
template<class C> void maxi(C&a4, C b4) { a4 = max(a4, b4); }

struct node{
    bool tak;
    int next[30];
};
#define maxn 100005
node T[maxn];
int root = 1;
int ile = 1;

int create() {
    ++ile;
    return ile;
}
const LL mod = 1000000007;

void dodaj(VI a) {
    int act = root;
    FORE(it, a) {
        if (T[act].next[*it] == 0) T[act].next[*it] = create();
        act = T[act].next[*it];
    }
    T[act].tak = 1;
}

int n, s;

LL sil[maxn];

LL pot(LL a, LL n) {
    if (n == 0) return 1;
    if (n % 2) {
        LL x = pot(a, n - 1);
        return (a * x) % mod;
    } else {
        LL x = pot(a, n / 2);
        return (x * x) % mod;
    }
}

LL odw(LL a) {
    return pot(a, mod - 2);
}

LL newt(int n, int k) {
    return (((sil[n] * odw(sil[k])) % mod) * odw(sil[n - k])) % mod;
}
LL suma = 0;

pair<LL, LL> dfs(int act) {
    vector<pair<int, LL> > u;
    LL su = 0;
    int ma = 0;
    int mi = INF;
    fup(i, 0, 30 - 1) {
        if (T[act].next[i]) {
            pair<LL, LL> q = dfs(T[act].next[i]);
            if (DEBUG)cout << "ADD " << act << " " << T[act].next[i] << " " << q.FI << " " << q.SE << endl;
            u.PB(q);
        }
    }

    if (T[act].tak) {
        u.PB(MP(1, -1));
    }
    if (siz(u) > 1) {
        if (DEBUG) cout << "DFS " << act << endl;
        FORE(it, u) {
            if (DEBUG)cout << it -> FI << " " << it -> SE << endl;
        }
        if (DEBUG) cout << "FFF " << endl;
    }

    FORE(it, u) {
        su += it -> FI;
        maxi(ma, it -> FI);
        mini(mi, it -> FI);
    }
    suma += min(su, LL(n));


    if (su < n) {
        return MP(su, -1);
    } else {
        if (ma < n) {
            LL ile_mr = 0; 
            LL ile_last = 0;
            fup(i, ma, n) {
                LL x = newt(n, i); 
                x %= mod;
                if (DEBUG)cout << "DOK " << i << " " << x << endl;
                FORE(it, u) {
                    x *= (newt(i, it -> FI) * sil[it -> FI]) % mod;
                    x %= mod;
                }
                debug(x);
                ile_last = x - ile_last;
                ile_mr += ile_last;
                ile_last += mod;
                ile_mr += mod;
                ile_last %= mod;
                ile_mr %= mod;
                debug(ile_last);
                debug(ile_mr);
            }
            if (DEBUG) cout << "HARDY " << ile_last << endl;
            return MP(su, ile_last);
        } else {
            LL il = 1;
            FORE(it, u) {
                if (it -> FI < n) il *= (newt(n, it -> FI) * sil[it -> FI]) % mod;
                else il *= it -> SE;
                il %= mod;
            }
            if (DEBUG) cout << "CHUJ " << act << endl;
            return MP(su, il);
        }
    }
}

void solve(int tcas) {
    cout << "Case #" << tcas << ": ";
    cin >> s >> n;
    CLR(T);
    ile = 1;

    fup(i, 1, s) {
        string a;
        cin >> a;
        VI u;
        FORE(it, a) u.PB((*it) - 'A');
        dodaj(u);
    }

    suma = 0;
    pair<int, LL> res = dfs(1);
    debug(suma);
    if (res.SE == -1) res.SE = 1;
    res.SE += 10 * mod;
    res.SE %= mod;
    cout << suma << " " << res.SE << endl;
}

int main(){
    sil[0] = 1;
    fup(i, 1, maxn - 1) sil[i] = (sil[i - 1] * i) % mod;
    ios_base::sync_with_stdio(false);
    int cas;
    cin >> cas;
    fup(c, 1, cas) {
        solve(c);
    }
    return 0;
}

