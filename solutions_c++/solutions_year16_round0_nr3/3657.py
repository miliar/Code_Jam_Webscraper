#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <stack>
#include <cmath>
#include <map>
#include <algorithm>
#include <string>

using namespace std;
typedef long long ll;
const int S=10;

ll change(ll x,ll bi);
ll isprime(ll x);
ll to2(ll x);

int main()
{
    //freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cass=1;
    while(t--)
    {
        int n,j;
        scanf("%d%d",&n,&j);
        printf("Case #%d:\n",cass++);
        int cnt=0;
        n--;
        ll ss=(1<<n)+1;
        ll up=1<<(n+1);
        //cout<<ss<<" "<<up<<endl;
        while(ss<up)
        {
            ll s=to2(ss);
            //cout<<s<<endl;
            if(cnt==j) break;
            int f=1;
            for(int i=2; i<=10; i++)
            {
                ll tmp=change(s,(ll)(i));
                if(isprime(tmp)==-1)
                {
                    f=0;
                    break;
                }
            }
            if(f==0)
            {
                ss+=2;
                continue;
            }
            else
            {
                cnt++;
                printf("%lld",s);
                for(int i=2; i<=10; i++)
                {
                    ll tmp=change(s,(ll)(i));
                    printf(" %lld",isprime(tmp));
                    //printf(" %lld",tmp);
                }
                printf("\n");
                ss+=2;
            }
        }

    }
    return 0;
}

ll to2(ll x)
{
    int tmp[30]= {0};
    int loca=0;
    while(x)
    {
        tmp[loca++]=x%2;
        x/=2;
    }
    ll ans=0;
    for(int i=loca-1; i>=0; i--)
        ans=ans*10+tmp[i];
    return ans;
}

ll isprime(ll x)
{
    for(ll i=2; i*i<=x; i++)
    {
        if(x%i==0) return (ll)(i);
    }
    return -1;
}

ll change(ll x,ll bi)
{
    ll tt=0,cnt=1;
    while(x)
    {
        tt+=x%10*cnt;
        cnt*=bi;
        x/=10;
    }
    return tt;
}
