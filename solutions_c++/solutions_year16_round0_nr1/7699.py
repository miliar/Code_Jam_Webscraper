#include<bits/stdc++.h>
#define pf printf
#define sf scanf
#define ll  long long
#define llu unsigned long long
#define M 10000
#define pb push_back
#define ppb pop_back
#define F first
#define S second
#define Check(x,w) (x&(1<<w))==(1<<w)?true:false
#define pii pair<ll,ll>
#define X 5800000
#define PI acos(-1)
#define MOD 100000000
using namespace std;

template<class T>
inline bool fs(T &x)
{
    int c=getchar();
    int sgn=1;
    while(~c&&c<'0'||c>'9')
    {
        if(c=='-')sgn=-1;
        c=getchar();
    }
    for(x=0; ~c&&'0'<=c&&c<='9'; c=getchar())
        x=x*10+c-'0';
    x*=sgn;
    return ~c;
}

bool ara[15];

int main()
{
    freopen("inAL.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt;
    ll a,b,c,d,e,g,i,j;
    fs(tt);
    for(t=1; t<=tt; t++)
    {
        fs(a);
        memset(ara,false,sizeof(ara));
        b=d=0;
        for(i=1; i<=M; i++)
        {
            c=a*i;
            while(c>0)
            {
                if(!ara[c%10])
                {
                    b++;
                    ara[c%10]=true;
                }
                c/=10;
            }
            if(b==10)
            {
                d=a*i;
                break;
            }
        }
        if(d==0)
            pf("Case #%d: INSOMNIA\n",t);
        else
            pf("Case #%d: %lld\n",t,d);
    }
    return 0;
}
