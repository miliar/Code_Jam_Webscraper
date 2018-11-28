#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
//#include<ctime>

using namespace std;
typedef long long ll;
const int test = 15; //测试次数

ll random(ll a,ll b){ // 返回[a,b)区间内的随机数
    return rand() % (b - a) + a;
    //return (ll)((double)rand()*(b - a)/RAND_MAX + 0.5) + a;
}

ll mod_mul(ll a,ll b,ll mod){
    ll res = 0;
    while(b){
        if(b & 1) res = (res + a) % mod;
        a = (a + a) % mod;
        b >>= 1;
    }
    return res;
}

ll mod_pow(ll a,ll b,ll mod){
    ll res = 1;
    while(b){
        if(b & 1) res = mod_mul(res,a,mod);
        a = mod_mul(a,a,mod);
        b >>= 1;
    }
    return res;
}

bool miller_rabin(ll n) {
    if(n == 2 || n == 3 || n == 5 || n == 7 || n == 11)    return true;
    if(n == 1 || !(n%2) || !(n%3) || !(n%5) || !(n%7) || !(n%11))    return false;

    ll x, pre, u;
    int i, j, k = 0;
    u = n - 1;    //要求x^u % n

    while(!(u&1)) {    //如果u为偶数则u右移，用k记录移位数
        k++; u >>= 1;
    }

    //srand((ll)time(NULL));
    for(i = 0; i < test; ++i) {    //进行S次测试
        x = random(2,n);    //在[2, n)中取随机数
        if((x%n) == 0)    continue;

        x = mod_pow(x, u, n);    //先计算(x^u) % n，
        pre = x;
        for(j = 0; j < k; ++j) {    //把移位减掉的量补上，并在这地方加上二次探测
            x = mod_mul(x, x, n);
            if(x == 1 && pre != 1 && pre != n-1)    return false;    //二次探测定理，这里如果x = 1则pre 必须等于 1，或则 n-1否则可以判断不是素数
            pre = x;
        }
        if(x != 1)    return false;    //费马小定理
    }
    return true;
}

ll gcd(ll a,ll b){
    if(a == 0) return 1;
    if(a < 0) return gcd(-a,b);
    while(b){
        ll t = a % b;
        a = b;
        b = t;
    }
    return a;
}

ll pollard_rho(ll n,ll c){
    ll x,y,d,i=1,k=2;
    x = random(1,n);
    y = x;
    while(1){
        i++;
        x = (mod_mul(x,x,n) + c) % n;
        d = gcd(y - x,n);
        if(d != 1 && d != n) return d;
        if(y == x) return n;
        if(i == k){
            y = x;
            k <<= 1;
        }
    }
}

bool findfac(ll n,ll &c){
    if(n == 1) return 0;
    if(miller_rabin(n)){
        c = n;
        return 1;
    }
    ll p = n;
    while(p >= n) p = pollard_rho(p,random(1,n));
    return findfac(p,c)|findfac(n/p,c);
}

/*int main(){
    int cas;
    scanf("%d",&cas);
    ll n;
    while(cas--){
        scanf("%lld",&n);
        if(miller_rabin(n)) printf("Prime\n");
        else{
            ans = 1ll<<60ll;
            findfac(n);
            printf("%lld\n",ans);
        }
    }
    return 0;
}*/

int n,m;
ll a,b,c[11];

void sol(){
    int i,j,cnt,S,Ed = 1<<(n-2);
    for(S = 0;S < Ed&&m>0;S++){
        cnt = 0;
        for(i = 2;i <= 10;i++){
            a = 1;
            b = i;
            for(j = 0;j < n-2;j++,b *= i){
                if(S>>j&1) a += b;
            }
            a += b;
            if(!miller_rabin(a)){
                cnt++;
                findfac(a,c[i]);
            }
//printf("%d %d %I64d\n",S,i,a);
        }
//printf("%d %d\n",S,a);
        if(cnt==9){
            printf("1");
            for(j = n-3;j >= 0;j--) printf("%d",S>>j&1);
            printf("1");
            for(i = 2;i <= 10;i++) printf(" %I64d",c[i]);
            putchar('\n');
            m--;
        }
    }
}

int main(){
    int i,j,cas;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&cas);
    for(int T=1;T<=cas;T++){
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",T);
        sol();
    }

    return 0;
}
