#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>

using namespace std;

typedef long long LL;

const int Maxn = 1000010;

LL ans[20];
int num[20];

int prime[Maxn];
int flag[Maxn];
int cnt;
void _init()
{
    for(int i = 2;i < Maxn;i ++)
    {
        if(!flag[i])
        {
            prime[cnt ++] = i;
            for(int j = i * 2;j < Maxn;j += i)
            {
                flag[j] = true;
            }
        }
    }
}
LL mul(LL x,LL y,LL mod)
{
    LL rt=0;
    if(x>mod) x%=mod;
    while(y)
    {
        if(y&1)
        {
            rt+=x;
            if(rt>=mod) rt-=mod;
        }
        x<<=1;
        if(x>=mod) x-=mod;
        y>>=1;
    }
    return rt;
}

LL exp(LL x,LL y,LL mod)
{
    LL rt=1;
    if(x>mod) x%=mod;
    while(y)
    {
        if(y&1)
        {
            rt=mul(rt,x,mod);
        }
        x=mul(x,x,mod);
        y>>=1;
    }
    return rt;
}

bool Witness(LL a,LL n)
{
    LL m=n-1,u,t=0;
    while(m%2==0) m/=2,t++;
    u=(n-1)/(1<<t);
    LL x=exp(a,u,n);
    while(t--)
    {
        LL y=x;
        x=mul(x,x,n);
        if(x==1 && y!=1 && y!=n-1) return true;
    }
    if(x!=1) return true;
    return false;
}

bool Miller_Rabin(LL n)
{
    if(n==2) return true;
    if(n<2) return false;
    if(n%2==0) return false;
    int text=20;
    while(text--)
    {
        LL a=rand()%(n-2)+2;
        if(Witness(a,n)) return false;
    }
    return true;
}

LL getRealVal(int n,int k)
{
    LL ans = 0;
    LL f = 1;
    while(n)
    {
        if(n & 1)
            ans += f;
        f = f * k;
        n >>= 1;
    }
    return ans;
}
int getPrime(LL n)
{
    for(int i = 0;i < cnt;i ++)
    {
        if(n % prime[i] == 0)
            return prime[i];
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    _init();
    int T ,N,J;
    cin>>T;
    for(int cas = 1;cas <= T;cas ++)
    {
        cin>>N>>J;
        cout<<"Case #"<<cas<<":"<<endl;
        for(int i = (1<<(N - 1)) + 1;;i += 2)
        {

            int k;
            for(k = 2;k <= 10;k ++)
            {
                ans[k] = getRealVal(i,k);
                //cout<<"ans["<<k<<"] = "<<ans[k]<<endl;
                if(Miller_Rabin(ans[k]))
                    break;
            }
            if(k > 10)
            {
                int tmp = i;
                int cnt = 0;
                while(tmp)
                {
                    num[cnt++] = tmp & 1;
                    tmp >>= 1;
                }
                for(int i = N - 1;i >= 0;i --)
                    cout<<num[i];

                for(int k = 2;k <= 10;k ++)
                {
                    cout<<" "<<getPrime(ans[k]);
                }
                cout<<endl;
                J--;
            }
            if(J <= 0)
                break;
        }

    }


    return 0;
}
