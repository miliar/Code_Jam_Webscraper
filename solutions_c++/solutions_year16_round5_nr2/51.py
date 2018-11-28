
#include <bits/stdc++.h>
#define int long long
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i < _a; ++i)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR(A,n)  { cout << #A << " = "; FOR(_,1,n) cout << A[_] << ' '; cout << endl; }
#define PR0(A,n) { cout << #A << " = "; REP(_,n) cout << A[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
#define ll long long
#define __builtin_popcount __builtin_popcountll
#define SZ(x) ((int) (x).size())
using namespace std;

double safe_sqrt(double x) {
    return sqrt(max((double)0.0,x));
}
int GI(ll& x) {
    return scanf("%lld", &x);
}

const int MN = 111;
const int MAX = 100111;
vector<int> ra[MN];
int vao[MN];
int n;
int nxt[MN];

void init(const string &p) {
    int l = SZ(p);
    nxt[0] = -1;
    int j = -1;
    FOR(i,1,l-1) {
        while (j >= 0 && p[j+1] != p[i]) j = nxt[j];
        if (p[j+1] == p[i]) ++j;
        nxt[i] = j;
    }
}

bool check(const string& s, const string& p) {
    int ls = SZ(s);
    int lp = SZ(p);
    int j = -1;

    REP(i,ls) {
        while (j >= 0 && p[j+1] != s[i]) j = nxt[j];
        if (p[j+1] == s[i]) ++j;

        if (j == lp-1) {
            return true;
        }
    }
    return false;
}

int w[111];

int dfs(int u) {
    if (w[u] >= 0) return w[u];

    w[u] = 1;
    for(int v : ra[u]) {
        w[u] += dfs(v);
    }
    return w[u];
}

string queries[111];

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n;
        FOR(i,1,n) ra[i].clear();
        FOR(i,1,n) {
            cin >> vao[i];
            if (vao[i]) ra[vao[i]].push_back(i);
        }
        string name; cin >> name; name = " " + name + " ";
        int q; cin >> q;
        FOR(i,1,q) cin >> queries[i];

//        if (test <= 50) continue;

        memset(w, -1, sizeof w);
        FOR(i,1,n) w[i] = dfs(i);

        cout << "Case #" << test << ":";
        FOR(i,1,q) {
            string pat = queries[i];
            int cnt = 0;
            init(pat);
            REP(turn,MAX) {
                vector<int> cur;

                FOR(i,1,n) if (!vao[i]) {
                    cur.push_back(i);
                }
                string s;

                REP(x,n) {
                    int sumw = 0;
                    for(int u : cur) sumw += w[u];

                    int dice = rand() % sumw;
                    int sum = dice;
                    int id = -1;

                    REP(pos,SZ(cur)) {
                        int u = cur[pos];
                        sum -= w[u];
                        if (sum < 0) {
                            id = pos;
                            break;
                        }
                    }
                    int u = cur[id];

                    s += name[u];

                    swap(cur[id], cur[SZ(cur)-1]);
                    cur.pop_back();

                    for(auto v : ra[u]) {
                        cur.push_back(v);
                    }
                }

                if (check(s, pat)) ++cnt;
            }
            cout << ' ' << cnt / (double) MAX;
        }
        cout << endl;
        cerr << test << endl;
    }
}
