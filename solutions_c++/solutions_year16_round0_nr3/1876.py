#include <cassert>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef __int128 LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define debug(args...) {vector<string> _v = split(#args, ','); err(_v.begin(), args); puts("");}
vector<string> split(const string& s, char c) {vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.emplace_back(x); return move(v);}
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) {cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", "; err(++it, args...);}

#define pb push_back
#define mp make_pair
#define all(x)  (x).begin(),(x).end()
#define tr(c, it)   for(auto it=c.begin(); it!=c.end(); it++)
#define clr(a, b)   memset(a, b, sizeof(a))

LL product_mod(LL a,LL p,LL mod){
    LL r = 0;
    while(p){
        if(p&1) r = (r+a)%mod;
        a = (a+a)%mod;
        p>>=1;
    }
    return r;
}

LL power_mod(LL a,LL p,LL mod){
    LL r = 1;
    while(p){
        if(p&1) r = r * a % mod;
        a = a * a % mod;
        p>>=1;
    }
    return r;
}

LL gcd(LL a, LL b){
    return b?gcd(b, a%b): a;
}

//1
LL pollard_rho(LL c,LL n)//某个因子,返回n失败
{
    int i=1,k=2;
    LL x=rand()%n, y=x;
    do{
        i++;
        LL d = gcd(n+y-x,n);
        if(d>1 && d<n)  return d;
        if(i==k)    y=x,k*=2;
        x = (product_mod(x,x,n)+n-c)%n;
    }
    while(y!=x);
    return n;
}

bool isprime(LL n)
{
    if(n==2)return true;
    if(n<2 || !(n&1))return false;
    int i,j,k = 0;
    LL pri[111] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541};
    LL a,m = n-1;
    while(m % 2 == 0) m>>=1,k++;
    for(i=0; i<11; i++)
    {
        if(pri[i]>=n)   return true;
        a = power_mod(pri[i], m, n);
        if(a == 1) continue;
        for(j=0; j<k; j++)
        {
            if(a == n-1)    break;
            a = product_mod(a,a,n);
        }
        if(j==k)    return false ;
    }
    return true;
}
int T;
int n, c;

map<LL, vector<LL> > fac;

bool check(LL x)
{
    fac[x] = vector<LL>();
    for(int base=2; base<=10; base++)
    {
        __int128 v = 0;
        __int128 b = 1;

        for(int i=0; i<n; i++)
        {
            if( (1ll << i) & x)
            {
                v += b;
            }
            b *= base;
        }

        if(isprime(v))
            return false;

        LL f = 0;
        for(int i=2; i<=1000;i++)
            if(v % i == 0)
            {
                f = i;
                break;
            }

        if(f == 0) return false;

        assert(v % f == 0);
        fac[x].push_back(f);
    }

    return true;
}

void print_bin(LL v, int n)
{
    for(int i=n-1; i>=0; i--)
    {
        int vv = (1ll << i) & v;
        if(vv) printf("1");
        else printf("0");
    }
    printf(" ");
}

int main()
{
#ifdef LOCAL
    //freopen("in", "r", stdin);

    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("out", "w", stdout);
#endif

    int cas = 1;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d%d",&n, &c);
        printf("Case #%d:\n", cas++);

        LL st = (1ll << (n - 1)) | 1;
        LL ed = (1ll << n) - 1;
        int cnt = 0;
        for(LL i=st; i<=ed; i+=2)
        {
            if(check(i))
            {
                cnt++;
                //debug(c);
                print_bin(i, n);
                //printf("%d\n", fac[i].size());
                tr(fac[i], it)
                {
                    long long val = (long long) *it;
                    printf("%lld%c", val, it == fac[i].end() - 1 ? '\n': ' ');
                }
                if(cnt >= c) break;
            }
        }
    }

    return 0;
}
