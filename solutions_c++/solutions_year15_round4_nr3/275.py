//Coder: Balajiganapathi
#ifndef ONLINE_JUDGE
#   define DEBUG
//#   define TRACE
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
const int mx = 202, mx_words = 2000 + 10 * mx + 100;

map<string, int> idx;
int idx_cnt;
vi s[mx];
int n;
int ans;
int cnt[2][mx_words];
string inv[mx_words];

#define set(mask, n) ((mask >> n) & 1)

void rec(int i, int cur = 0) {
    if(i == n) {
        trace1(cur);
        ans = min(ans, cur);
        return;
    }

    fo(l, 2) {
        if(i == 0 && l == 1) continue;
        if(i == 1 && l == 0) continue;

        int nw = 0;
        fo(j, si(s[i])) {
            ++cnt[l][s[i][j]];
            if(cnt[l][s[i][j]] == 1 && cnt[1 - l][s[i][j]] > 0) {
                trace5(i, l, s[i][j], inv[s[i][j]], nw);
                ++nw;
            }
        }
        rec(i + 1, cur + nw);
        fo(j, si(s[i])) {
            --cnt[l][s[i][j]];
        }
    }
}

int main() {
    //freopen("sample.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    freopen("C-small-attempt0.in", "r", stdin);
    freopen("small0.txt", "w", stdout);

    //freopen("C-large.in", "r", stdin);
    //freopen("large.txt", "w", stdout);
    
    int kases;
    scanf("%d", &kases);
    for(int kase = 1; kase <= kases; ++kase) {
        scanf("%d", &n);
        idx.clear();
        idx_cnt = 0;
        string line;
        getline(cin, line);
        fo(i, n) {
            s[i].clear();
            getline(cin, line);
            trace2(i, line);
            istringstream iss(line);
            string word;
            while(iss >> word) {
                if(!idx[word]) {
                    idx[word] = ++idx_cnt;
                    inv[idx_cnt] = word;
                }
                s[i].pu(idx[word]);
                trace3(i, word, idx[word]);
            }
        }

        ans = oo;
        ini(cnt, 0);
        rec(0);

        printf("Case #%d: %d\n", kase, ans);
    }
    
	return 0;
}
