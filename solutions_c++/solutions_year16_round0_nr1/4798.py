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

#define OK printf("ok\n")
#define DB(x) cout << #x << " = " << x << endl;

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> pii;

int setBit(int N, int pos) { return N=N | (1<<pos); }
int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }

//int kx[] = {+2, +1, -1, -2, -2, -1, +1, +2};
//int ky[] = {+1, +2, +2, +1, -1, -2, -2, -1}; //Knight Direction
//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction

bool visit[11];
LL cnt;

inline void cover(LL n) {
    while(n) {
        LL x = n%10;
        n /= 10;
        if(!visit[x]) {
            visit[x] = true;
            cnt++;
        }
    }
}

LL fuck(LL n) {
    LL nn = n;
    cover(nn);
    while(true) {
        if(cnt == 10) return nn;
        nn += n;
        cover(nn);
    }
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);

    LL test, kase=1, n;

    sdl(test);
    while(test--) {
        sdl(n);
        printf("Case #%lld: ", kase++);
        if(n==0) {
            puts("INSOMNIA");
            continue;
        }
        mem(visit, false);
        cnt=0;
        pfl(fuck(n));
    }


//    repl(n, 1000000) {
//        mem(visit, false);
//        cnt=0;
//        pfl(fuck(n));
//        if(n%1000 == 0) fprintf(stderr, "%d\n", n);
//    }

    return 0;
}
