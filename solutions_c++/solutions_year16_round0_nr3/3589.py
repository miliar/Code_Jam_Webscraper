#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define rep2(i, j, k) for(int i = (int) j; i >= (int) k; --i)
#define ll long long
#define mp make_pair
using namespace std;

const int N = 19;
int n, J;

int pri[]={2,3,5,7,11,13,17,19,23,29};
ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}

ll mul(ll a, ll b, ll M){
    ll r = 0;
    while(b) {
        if(b & 1) { r += a; if(r >= M) r -= M; }
        a <<= 1; if(a >= M) a -= M;
        b >>= 1;
    }
    return r;
}
ll pow(ll a, ll b, ll M){
    ll r = 1;
    a %= M;
    while(b){
        if(b & 1) r = mul(r, a, M);
        a = mul(a, a, M);
        b >>= 1;
    }
    return r;
}
//
bool Miller_Rabin(ll n)
{
    if(n < 2) return false;
    if(n == 2) return true;
    if(!(n&1)) return false;
    ll k = 0, i, j, m, a;
    m = n - 1;
    while(!(m&1)) m >>= 1, k++;
    for(i = 0; i < 10; i++){
        if(pri[i] >= n) return true;
        a = pow(pri[i], m, n);
        if(a == 1) continue;
        for(j = 0; j < k; j++){
            if(a == n-1) break;
            a = mul(a, a, n);
        }
        if(j == k) return false;
    }
    return true;
}
ll pollard_rho(ll c, ll n)
{
    ll i, x, y, k, d;
    i = 1;
    x = y = rand() % n;
    k = 2;
    do{
        i++;
        d = gcd(n+y-x, n);
        if(d>1 && d<n) return d;
        if(i == k) y = x, k <<= 1;
        x = (mul(x, x, n) + n - c) % n;
    }while(y != x);
    return n;
}

ll fac[1000], ct;
void rho(ll n)
{
    if(Miller_Rabin(n)) {
        fac[ct++] = n;
        return ;
    }
    ll t = n;
    while(t >= n) t = pollard_rho(rand() % (n-1) + 1, n);
    rho(t);
    rho(n / t);

}


ll base[11][N];

void initt() {
    rep(i, 1, 11) {
        base[i][0] = 1;
        rep(j, 1, N) base[i][j] = base[i][j-1] * i;
    }
    return ;
}

ll value[11];

void solve() {
    memset(value, 0, sizeof value);
    rep(i, 2, 11) value[i] = base[i][n-1] + base[i][0];
    int shift = 1 << (n-2);
    int ba[N] = {0};
    ll divisor[N];
    memset(divisor, 0, sizeof divisor);
    bool flag;
    int cntt = 0;
    rep2(i, shift-1, 1) {
        int k = i, le = 1;
        flag = 1;
        memset(ba, 0, sizeof ba);
        while(k) ba[le++] = k&1, k >>= 1;
        rep(p, 2, 11) {
            ll v = value[p];
            rep(j, 1, n-1) v += base[p][j] * ba[j];
            if(Miller_Rabin(v)) {
                flag = 0;
                break;
            }
            else {
                ct = 0;
                rho(v);
//                sort(fac, fac+ct);
                divisor[p] = fac[0];
            }
        }
        if(!flag) continue;
//rep(j, 1, n-1) printf("%d ", ba[j]); puts("+++++");
//rep(p, 2, 11) {
//    ll vv = value[p];
//    rep(j, 1, n-1) vv += ba[j]*base[p][j];
//    printf("vv = %lld  divi:%lld  vvmoddiv:%lld  vv/div:%lld\n", vv, divisor[p], vv % divisor[p], vv/divisor[p]);
//
//}
        ++cntt;
        printf("1"); rep2(j, n-2, 1) printf("%d", ba[j]); printf("1 ");
        rep(j, 2, 11) printf(" %lld", divisor[j]); puts("");
        if(cntt == J) break;
    }
    return ;
}

int main()
{
#ifdef PIT
freopen("C-small-attempt2.in", "r", stdin);
freopen("C-small-attempt1.out", "w", stdout);
#endif // PIT
    initt();
    int T, ic = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%d %d", &n, &J);
        printf("Case #%d:\n", ic++);
        solve();
    }
    return 0;
}
