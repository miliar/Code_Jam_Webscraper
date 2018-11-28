#include <cstdio>
#include <cstring>
#include <algorithm>
#include <climits>
#include <cctype>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <iostream>
#include <vector>
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <string>
#define pu system("pause")
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const double pi = acos(-1.0);
const int inf = 0x7fffffff;
const int mod = 1e8 + 7;

struct node
{
    ll x;
    ll ans[15];
}res[510];



const int S = 8;
long long mult_mod(long long a,long long b,long long c)
{
a %= c;
b %= c;
long long ret = 0;
long long tmp = a;
while(b)
{
if(b & 1)
{
ret += tmp;
if(ret > c)ret -= c;
}
tmp <<= 1;
if(tmp > c)tmp -= c;
b >>= 1;
}
return ret;
}
long long pow_mod(long long a,long long n,long long mod)
{
long long ret = 1;
long long temp = a%mod;
while(n)
{
if(n & 1)ret = mult_mod(ret,temp,mod);
temp = mult_mod(temp,temp,mod);
n >>= 1;
}
return ret;
}

bool check(long long a,long long n,long long x,long long t)
{
long long ret = pow_mod(a,x,n);
long long last = ret;
for(int i = 1;i <= t;i++)
{
ret = mult_mod(ret,ret,n);
if(ret == 1 && last != 1 && last != n-1)return true;
last = ret;
}
if(ret != 1)return true;
else return false;
}
bool Miller_Rabin(long long n)
{
if( n < 2)return false;
if( n == 2)return true;
if( (n&1) == 0)return false;
long long x = n - 1;
long long t = 0;
while( (x&1)==0 ){x >>= 1; t++;}
srand(time(NULL));
for(int i = 0;i < S;i++)
{
long long a = rand()%(n-1) + 1;
if( check(a,n,x,t) )
return false;
}
return true;
}

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("out","w",stdout);
    int t,k = 1;
    scanf("%d",&t);
    while (t --)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",k ++);
        int cnt = 0;
        for (ll i = ((ll)1 << (n - 1));i <= ((ll)1 << n) - 1 && cnt < m; ++ i)
        {
            ll x = i;


            if ((x & 1) && (x & (1 << (n - 1))))
            {
//                printf("x = %lld\n",x);
//    //            pu;
//                for (int j = n - 1;j >= 0; -- j)
//                {
//                    printf("%d",((1 << j) & x) > 0 ? 1 : 0);
//                }
//                puts("");
                bool flag = 1;
                node temps;
                temps.x = x;
                for (int j = 2;j <= 10; ++ j)
                {
                    ll cur = 1;
                    ll checks = 0;
                    ll temp = x;
                    while (temp)
                    {
                        checks += cur * (temp & 1);
                        temp >>= 1;
                        cur *= j;
                    }
//                    printf("j = %d checks = %lld\n",j,checks);
                    if (Miller_Rabin(checks))
                    {
                        flag = 0;
                        break;
                    }
                    temps.ans[j] = checks;
                }
                if (flag)
                {
                    res[cnt ++] = temps;
                }
            }
        }
        for (int i = 0;i < cnt; ++ i)
        {
//            printf("x = %lld\n",res[i].x);
            for (int j = n - 1;j >= 0; -- j)
            {
                printf("%d",((1 << j) & res[i].x) > 0 ? 1 : 0);
            }
            printf(" ");
            for (int j = 2;j <= 10; ++ j)
            {
                for (int p = 2;p < res[i].ans[j]; ++ p)
                {
                    if (res[i].ans[j] % p == 0)
                    {
                        printf("%d%c",p,j == 10 ? '\n' : ' ');
                        break;
                    }
                }
            }
        }
    }
    return 0;
}
