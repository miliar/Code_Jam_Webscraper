//Coder: Balajiganapathi
#define TRACE
#define DEBUG

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
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

// Basic macros
#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define rep(i,s,n)  for(int i=s;i<=(n);++i)
#define fr(i,n)     re(i,0,n)
#define repv(i,f,t) for(int i = f; i >= t; --i)
#define rev(i,f,t)  repv(i,f - 1,t)
#define frv(i,n)    rev(i,n,0)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

const int oo = 2000000009;
const double eps = 1e-9;

#ifdef TRACE
    #define trace1(x)                cerr << #x << ": " << x << endl;
    #define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
    #define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
    #define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
    #define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
    #define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

    #define trace1(x)
    #define trace2(x, y)
    #define trace3(x, y, z)
    #define trace4(a, b, c, d)
    #define trace5(a, b, c, d, e)
    #define trace6(a, b, c, d, e, f)

#endif

const int mx = 8;
int cost[(1 << mx)], n, m;
string s[mx];
int ans, cnt;
int server[mx];

int calc(int mask) {
    set<string> nodes;
    nodes.insert("");
    fr(i, n) if(mask & (1 << i)) {
        fr(len, sz(s[i]) + 1) nodes.insert(s[i].substr(0, len));
    }
    return sz(nodes);
}

void solve(int cur) {
    if(cur == n) {
        int c = 0;
        fr(i, m) if(!server[i]) return;
        fr(i, m) c += cost[server[i]];
        if(c > ans) {
            ans = c;
            cnt = 1;
        } else if(c == ans) {
            ++cnt;
        }
        return;
    }
    fr(nxt, m) {
        server[nxt] |= (1 << cur);
        solve(cur + 1);
        server[nxt] ^= (1 << cur);
    }
}

int main() {
    //freopen("sample.txt", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
    //freopen("D-large.in", "r", stdin);

    //freopen("output.txt", "w", stdout);
    freopen("small0.txt", "w", stdout);
    //freopen("large.txt", "w", stdout);
    
    int kases, kase;
    scanf("%d", &kases);
    for(kase = 1; kase <= kases; ++kase) {
        scanf("%d %d", &n, &m);
        fr(i, n) cin >> s[i];
        fr(mask, (1 << n)) cost[mask] = calc(mask);

        ans = -oo; cnt = 0;
        fr(i, m) server[i] = 0;
        solve(0);

        printf("Case #%d: %d %d\n", kase, ans, cnt);
    }
    
	return 0;
}
