#include <bits/stdc++.h>
using namespace std;
#define long int64_t
#define ulong uint64_t
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define cauto const auto
#define _overload3(_1,_2,_3,name,...) name
#define _rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload3(__VA_ARGS__,repi,_rep,)(__VA_ARGS__)
#define all(c) begin(c),end(c)
template<class C>inline void uniq(C&c){c.erase(unique(all(c)),end(c));}
template<class T>inline bool chmin(T&a,const T&b){return a>b&&(a=b,1);}
template<class T>inline bool chmax(T&a,const T&b){return a<b&&(a=b,1);}

const int N = 128;
const int M = 5;

int n, par[N];
vector<int> ch[N];

int m, len[M];
string s, y[M];

void input()
{
    cin >> n;
    rep(i, n) cin >> par[i+1];
    ++n;
    rep(i, n) ch[i].clear();
    rep(i, 1, n) ch[par[i]].push_back(i);
    cin >> s >> m;
    s = '~' + s;
    rep(i, m) cin >> y[i], len[i] = y[i].length();
}

int pat[M][128];

void generate_pattern()
{
    memset(pat, 0, sizeof(pat));
    rep(i, m) rep(j, len[i]) {
        pat[i][(int)y[i][j]] |= 1 << j;
    }
}

int size[N];

void recur(int v)
{
    for (const int c : ch[v]) {
        recur(c);
    }
    size[v] = 1;
    for (const int c : ch[v]) {
        size[v] += size[c];
    }
}

inline unsigned xor128() {
    static unsigned x = 123456789;
    static unsigned y = 362436069;
    static unsigned z = 521288629;
    static unsigned w =  88675123;
    unsigned t = x ^ (x << 11);
    return x = y, y = z, z = w, w ^= (w >> 19) ^ t ^ (t >> 8);
}

int pick_and_insert(vector<pair<int, int> >& que, int rest)
{
    const int k = que.size();
    int r = xor128() % rest;
    rep(i, k) {
        const auto& p = que[i];
        r -= p.first;
        if (r < 0) {
            const int ret = p.second;
            swap(que[i], que[k-1]);
            que.pop_back();
            for (const int c : ch[ret]) {
                que.emplace_back(size[c], c);
            }
            return ret;
        }
    }
    assert(false);
}

const string generate()
{
    vector<pair<int, int> > que;
    que.emplace_back(n, 0);
    string ret;
    rep(i, n) {
        const int p = pick_and_insert(que, n - i);
        if (i) ret.push_back(s[p]);
    }
    return ret;
}

int cnt[M];

void count(const string& s)
{
    const int k = s.length();
    int match[M] = {};
    bool ok[M] = {};
    rep(i, k) {
        rep(j, m) {
            match[j] = (match[j] << 1 | 1) & pat[j][(int)s[i]];
            ok[j] |= match[j] >> (len[j] - 1);
        }
    }
    rep(i, m) cnt[i] += ok[i];
}

void solve()
{
    recur(0);
    fill_n(cnt, m, 0);
    const int X = 100000;
    rep(_, X) count(generate());
    rep(i, m) {
        double ans = (double)cnt[i] / X;
        cout << " " << ans;
    }
    cout << endl;
}

int main()
{
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        input();
        generate_pattern();
        cout << "Case #" << i << ":";
        solve();
    }
}
