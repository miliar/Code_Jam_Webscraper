#include <bits/stdc++.h>

#define rep(i,n) for(i=0; i<n; i++)
#define repl(i,n) for(i=1; i<=n; i++)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin(); i!=(n).end(); i++)

#define sz(x) (int) x.size()
#define pb(x) push_back(x)
#define all(x) x.begin(),x.end()
#define uu first
#define vv second
#define mem(x, y) memset(x, y, sizeof(x));

#define sdi(x) scanf("%d", &x)
#define sdii(x, y) scanf("%d %d", &x, &y)
#define sdiii(x, y, z) scanf("%d %d %d", &x, &y, &z)
#define sdl(x) scanf("%lld", &x)
#define sdll(x, y) scanf("%lld %lld", &x, &y)
#define sdlll(x, y, z) scanf("%lld %lld %lld", &x, &y, &z)
#define sds(x) scanf("%s", x)
#define pfi(x) printf("%d\n", x)
#define pfii(x, y) printf("%d %d\n", x, y)
#define pfiii(x, y, z) printf("%d %d %d\n", x, y, z)
#define pfl(x) printf("%lld\n", x)
#define pfll(x, y) printf("%lld %lld\n", x, y)
#define pflll(x, y, z) printf("%lld %lld %lld\n", x, y, z)

#define eps 1e-9
#define OK printf("ok\n")
#define DB(x) cout << #x << " = " << x << endl;

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> pii;

inline int setBit(int N, int pos) { return N=N | (1<<pos); }
inline int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
inline bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }

//int kx[] = {+2, +1, -1, -2, -2, -1, +1, +2};
//int ky[] = {+1, +2, +2, +1, -1, -2, -2, -1}; //Knight Direction
//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction


LL n=16, tot=50, boob=14;

inline LL power(LL b, LL p) {
    LL ret=1;
    while(p) {
        if(p%2 == 1) {
            ret *= b;
//            ret %= MOD;
        }
        p /= 2;
        b = b*b;
//        b %= MOD;
    }
    return ret;
}

inline LL b(string s, LL b) {
    LL i, now=0;
    rep(i, n) {
        if(s[i] == '1') now += power(b, i);
    }
    return now;
}

inline LL primeFuck(LL x) {
    if(x<=3) return -1;
    LL i, loop=(LL)(sqrt(x)+1);
    for(i=2; i<=loop; i++) {
        if(x%i == 0) return i;
    }
    return -1;
}

inline bool here(string s) {
    LL i, j, ans[12];
    for(i=2; i<=10; i++) {
        LL x = b(s, i);
        LL y = primeFuck(x);
        if(y == -1) return false;
        else ans[i] = y;
    }
    reverse(all(s));
    printf("%s", s.c_str());
    for(i=2; i<=10; i++) printf(" %lld", ans[i]);
    puts("");
    return true;
}

inline string bin(LL x) {
    string ret;
    while(x) {
        ret += x%2 + '0';
        x /= 2;
    }
    LL now = boob-sz(ret);
    while(now--) ret += '0';
    reverse(all(ret));
    return ret;
}

void fuck() {
    LL i, loop=(1<<boob);
    rep(i, loop) {
        if(!tot) return;
        string s = "1" + bin(i) + "1";
        if(here(s)) tot--;
    }
}

int main() {
//    freopen("A-large.in","r",stdin);
    freopen("C-small.out","w",stdout);
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);

    puts("Case #1:");
    fuck();

    return 0;
}
