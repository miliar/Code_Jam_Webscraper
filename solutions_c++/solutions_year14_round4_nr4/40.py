#include <bits/stdc++.h>

using namespace std;

#define long int64_t

#define rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=a;i<(b);++i)
#define all(u) begin(u),end(u)
#define rall(u) (u).rbegin(),(u).rend()
#define uniq(u) (u).erase(unique(all(u)),end(u))

#define mp make_pair
#define pb push_back
#define eb emplace_back

const int sigma = 27;
const long mod = 1000000007;

long binom[128][128] = {1};

void prepare()
{
    repi(n, 1, 128) {
        binom[n][0] = 1;
        repi(k, 1, n + 1) {
            binom[n][k] = binom[n - 1][k - 1] + binom[n - 1][k];
            if (binom[n][k] >= mod) binom[n][k] -= mod;
        }
    }
}

long choose(int n, int k)
{
    return 0 <= k and k <= n ? binom[n][k] : 0;
}

long inex(int n, vector<int> v)
{
    long ret = 0;
    int sgn = 1;
    for (int k = n; k >= 1; --k) {
        long tmp = choose(n, k);
        for (int e : v) {
            tmp = tmp * choose(k, e) % mod;
        }
        ret = ((ret + sgn * tmp) % mod + mod) % mod;
        sgn = -sgn;
    }
    return ret;
}

int m, n;

struct node
{
    node *next_data[sigma];
    int size_data;
    long calc_data;
    node() : size_data(-1), calc_data(-1) {
        rep(i, sigma) next_data[i] = NULL;
    }
    ~node() {
        rep(i, sigma) if (next_data[i] != NULL) {
            delete next_data[i];
        }
    }
    node *next(char c) {
        const int id = c - 'A';
        if (next_data[id] == NULL) {
            next_data[id] = new node();
        }
        return next_data[id];
    }
    int size() {
        if (size_data >= 0) return size_data;

        int ret = 0;
        rep(i, sigma) if (next_data[i] != NULL) {
            ret += next_data[i]->size();
        }
        if (ret == 0) ret = 1;

        return size_data = min(n, ret);
    }
    long opt() {
        bool leaf = false;
        long ret = size();
        rep(i, sigma) if (next_data[i] != NULL) {
            leaf = true;
            ret += next_data[i]->opt();
        }
        return leaf ? ret : 0;
    }
    long calc() {
        if (calc_data >= 0) return calc_data;

        vector<int> v;
        rep(i, sigma) if (next_data[i] != NULL) {
            v.pb(next_data[i]->size());
        }
        long ret = inex(size(), v);

        // cerr << "inex of " << value << ' ' << ret << endl;

        rep(i, sigma) if (next_data[i] != NULL) {
            ret = ret * next_data[i]->calc() % mod;
        }

        // cerr << "calc of " << value << ' ' << ret << endl;

        return calc_data = ret;
    }
};

node *nil;

void add(string s)
{
    node *t = nil;
    rep(i, int(s.length())) {
        t = t->next(s[i]);
    }
    t = t->next('Z' + 1);
}

void input()
{
    nil = new node();

    cin >> m >> n;
    rep(i, m) {
        string s;
        cin >> s;
        add(s);
    }
}

void solve()
{
    cout << nil->opt() << ' ';
    cout << nil->calc() << endl;

    delete nil;
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    prepare();

    int T, cnt = 0;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << ++cnt << ": ";
        input();
        solve();
    }

    return 0;
}
