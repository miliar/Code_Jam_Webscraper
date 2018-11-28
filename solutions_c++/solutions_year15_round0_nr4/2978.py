/*
*Sourav Sen Tonmoy
*University of Dhaka
*/

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


int x, r, c;

bool fitable() {
    if(x <= 2) return true;
    int mn = min(r, c), mx = max(r, c);
    for(int i=x; i>=1; i--) {
        if(x-i+1 > i) break;
        if(i > mx || x-i+1 > mn) return false;
    }
    return true;
}

bool zLockable() {
    if(min(r, c) <= x-2) return true;
    else return false;
}

bool check() {
    if(!fitable()) return false;
    if(x > 3 && zLockable()) return false;
    if(x <= 6) {
        if(r*c%x == 0) return true;
        else return false;
    }
    else {
        if(min(r, c) >= 3) return false;
        else if(r*c%x == 0) return true;
        else return true;
    }
}

int main() {
    freopen("D-small.in","r",stdin);
    freopen("D-small-out.out","w",stdout);

//    freopen("D-dataset.in", "r", stdin);
//    freopen("D-dataset-out.out", "w", stdout);

    int test, kase=1;

    sdi(test);
    while(test--) {
        sdiii(x, r, c);
//        pfiii(x, r, c);
        printf("Case #%d: ", kase++);
        if(!check()) puts("RICHARD");
        else puts("GABRIEL");
    }

    return 0;
}
