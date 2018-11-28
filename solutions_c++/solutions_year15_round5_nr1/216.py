//Coder: Balajiganapathi
#ifndef ONLINE_JUDGE
#   define DEBUG
#   define TRACE
#else
//#   define NDEBUG
#endif

#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;
typedef vector<pi> vpi;

// Basic macros
#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define rep(i,s,n)  for(int i=s;i<=(n);++i)
#define fo(i,n)     re(i,0,n)
#define rev(i,n,s)  for(int i=(n)-1;i>=s;--i)
#define repv(i,n,s) for(int i=(n);i>=s;--i)
#define fov(i,n)    rev(i,n,0)
#define pu          push_back
#define mp          make_pair
#define si(x)       (int)(x.size())

#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
    #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
    #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
    #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
    #define trace4(a,b,c,d)
    #define trace5(a,b,c,d,e)
    #define trace6(a,b,c,d,e,f)
#endif

const int oo = 1000000009;
const double eps = 1e-6;
const int mod = 1000000007;
const int mx = 1000006;

int s[mx], m[mx], n, d;
vi child[mx];
int start[mx], end[mx], vis_time;

int seg[4 * mx], lazy[4 * mx];

void build(int i, int a, int b) {
    lazy[i] = 0;
    if(a == b) {
        seg[i] = 1;
        return;
    }
    int l = 2 * i + 1, r = 2 * i + 2, m = (a + b) / 2;
    build(l, a, m);
    build(r, m + 1, b);
    seg[i] = seg[l] + seg[r];
    assert(seg[i] == b - a + 1);
}

int get(int i, int a, int b, int qa, int qb) {
    if(qb < a || qa > b) return 0;
    if(lazy[i]) return 0;
    if(qa <= a && b <= qb) return seg[i];
    
    int l = 2 * i + 1, r = 2 * i + 2, m = (a + b) / 2;
    return get(l, a, m, qa, qb) + get(r, m + 1, b, qa, qb);
}

void update(int i, int a, int b, int qa, int qb) {
    if(qb < a || qa > b || lazy[i]) return;
    if(qa <= a && b <= qb) {
        lazy[i] = 1;
        seg[i] = 0;
        return;
    }

    int l = 2 * i + 1, r = 2 * i + 2, m = (a + b) / 2;
    update(l, a, m, qa, qb);
    update(r, m + 1, b, qa, qb);
    seg[i] = seg[l] + seg[r];
}

void dfs(int x) {
    start[x] = vis_time++;
    fo(i, si(child[x])) dfs(child[x][i]);
    end[x] = vis_time - 1;
}

int main() {
    //freopen("sample.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("small0.txt", "w", stdout);

    //freopen("A-large.in", "r", stdin);
    //freopen("large.txt", "w", stdout);
    
    int kases;
    scanf("%d", &kases);
    for(int kase = 1; kase <= kases; ++kase) {
        printf("Case #%d: ", kase);
        scanf("%d %d", &n, &d);
        int as, cs, rs;
        int am, cm, rm;
        scanf("%d %d %d %d", s + 0, &as, &cs, &rs);
        scanf("%d %d %d %d", m + 0, &am, &cm, &rm);
        //trace4(s[0], as, cs, rs);
        re(i, 1, n) {
            s[i] = (1ll * s[i - 1] * as + cs) % rs;
            //trace2(i, s[i]);
        }
        re(i, 1, n) m[i] = (1ll * m[i - 1] * am + cm) % rm;
        re(i, 1, n) m[i] %= i;
        //re(i, 1, n) trace3(i, m[i], s[i]);

        re(i, 1, n) child[m[i]].pu(i);

        vis_time = 0;
        dfs(0);
        assert(vis_time == n);

        vpi v;
        vi sv;
        fo(i, n) {
            v.pu(mp(s[i], i));
            sv.pu(s[i]);
        }
        sort(all(v));
        sort(all(sv));

        int ans = 1;

        fo(i, n) {
            //trace4(i, v[i].fi, v[i].se, sv[i]);
            build(0, 0, n - 1);
            fo(j, n) if(sv[j] < sv[i] || sv[j] > sv[i] + d) {
                //trace6(i, j, v[j].se, sv[j], start[v[j].se], end[v[j].se]);
                update(0, 0, n - 1, start[v[j].se], end[v[j].se]);
            }
            int cur = get(0, 0, n - 1, 0, n - 1);
            //trace2(i, cur);
            ans = max(ans, cur);
        }
        printf("%d\n", ans);
        fo(i, n) child[i].clear();
    }
    
	return 0;
}
