#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
#define rep(i,a,b) for(int i=(a),__tzg_##i=(b);i<__tzg_##i;++i)
#define urp(i,a,b) for(int i=(a),__tzg_##i=(b);i>=__tzg_##i;--i)
#define rp(i,b) rep(i,0,b)
#define repd(i,a,b) rep(i,a,(b)+1)
#define mst(a,b) memset(a,b,sizeof(a))
#define vrp(it,v) for(auto it(v.begin());(it)!=(v.end());++it)
#define vtr(v) (v).begin(),(v).end()
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
#define pb(a) push_back(a)
#define _0(x) (!(x))
#define _1(x) (x)
#define bit(x,y) (((x)>>(y))&1)
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;


struct MillerRabin {
    const static int Times = 20;

    ll add(ll a, ll b, ll mod) {
        return a+=b, a>=mod?a-mod:a;
    }
    //乘法，采用加法模拟，避免中间结果超出ll
    ll multi(ll a,ll b,ll mod) {
        ll res = 0;
        while(b) {
            if(b & 1) res = add(res, a, mod);
            a = add(a, a, mod);
            b >>= 1;
        }
        return res;
    }

    //快速幂，同样避免超出ll的做法
    ll pow(ll a, ll b, ll mod) {
        ll res = 1;
        while(b) {
            if (b & 1) res = multi(res, a, mod);
            a = multi(a, a, mod);
            b >>= 1;
        }
        return res;
    }

    //miller_rabin的一遍探测，返回1表示是合数
    int check(ll a, ll n, ll x, ll t) {
        ll ret = pow(a,x,n);
        ll last = ret;
        for(int i=1; i<=t; i++) {
            ret = multi(ret,ret,n);
            if(ret==1&&last!=1&&last!=n-1)
                return 1;//合数
            last=ret;
        }
        if(ret!=1)
            return 1;
        return 0;
    }

    //miller_rabin算法，返回false表示是合数，否则是素数
    //返回素数出错的概率(最高)为 1 / (4 ^ times)
    int miller_rabin(ll n) {
        if(n == 2) return 1;
        if( n<2 || !(n&1) ) return 0;
        ll x = n-1;
        ll t = 0;
        while( (x&1) == 0) {
            x>>=1;
            t++;
        }
        for(int i = 0; i < Times; i++) {
            ll a = rand()%(n-1)+1;
            if(check(a,n,x,t))
                return 0;//合数
        }
        return 1;
    }

    //************************************************
    //pollard_rho 算法进行质因数分解
    //************************************************
    ll factor[100];//质因数分解结果（刚返回时是无序的）
    int tol;//质因数的个数。数组小标从0开始

    ll gcd(ll a,ll b) {
        if(a==0)return 1;
        if(a<0) return gcd(-a,b);
        while(b) {
            ll t=a%b;
            a=b;
            b=t;
        }
        return a;
    }

    ll pollard_rho(ll x, ll c) {
        ll i = 1, k = 2;
        ll x0 = rand()%x;
        ll y = x0;
        while(1) {
            i++;
            x0=(multi(x0, x0, x) + c) % x;
            ll d = gcd(y-x0,x);
            if(d!=1&&d!=x) return d;
            if(y==x0) return x;
            if(i==k) {
                y = x0;
                k += k;
            }
        }
    }

    //对n进行素因子分解
    void find_fac_imp(ll n) {
        if(miller_rabin(n)) { //素数
            factor[tol++]=n;
            return;
        }
        ll p = n;
        while(p >= n) p=pollard_rho(p, rand()%(n-1)+1);
        find_fac_imp(p);
        find_fac_imp(n/p);
    }

    void findfac(ll n) {
        this->tol = 0;
        find_fac_imp(n);
    }
} ml;

int num[100];
ll res[15];
void solve() {
    int N, J;
    cin>>N>>J;
    ll top = 1ll<<(N-2);
    num[0] = num[N-1] = 1;
    int cnt = 0;
    for (ll mask = 0; mask < (top); ++mask) {
        for (int i = 0; i< N-2; ++i) {
            num[i+1] = (mask >> i) & 1;
        }
        int f = 1;
        for (int base = 2; base <= 10; ++base) {
            ll m = 0;
            for (int i = N-1; i >= 0; --i) {
                m = m * base + num[i];
            }
            ml.findfac(m);
            if (ml.tol == 1) {
                f = 0;
                break;
            }
            res[base] = (ml.factor[0]);
        }
        if (!f) continue;
        urp(i, N-1, 0) printf("%d", num[i] );
        for (int base = 2; base <= 10; ++base) {
            cout<<" "<<res[base];
        }
        puts("");
        ++cnt;
        if (cnt == J) break;
    }
}


int main() {
#ifdef _TZG_DEBUG
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif // _TZG_DEBUG
    int t;
    cin>>t;
    repd(_, 1, t) {
        printf("Case #%d:\n", _);
        solve();
    }
    return 0;
}
