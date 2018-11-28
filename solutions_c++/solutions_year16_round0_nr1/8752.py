#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

#define S(x) scanf("%d",&x)
#define S1(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define Sd(x) scanf("%lf",&x)
#define Pd(x) printf("%0.10lf\n",x)
#define P1(x) printf("%lld\n",x)
#define Ps(x) printf("%d ",x)
#define P1s(x) printf("%lld ",x)
#define St(x) scanf("%s",x)
#define Pt(x) printf("%s\n",x)
#define Sa(a,n) for(i=0;i<n;i++){scanf("%lld",&a[i]);}
#define Pa(a,n) for(i=0;i<n;i++){printf("%lld ",a[i]);}putchar('\n')
#define Y printf("YES\n")
#define N printf("NO\n")
#define mod 1000000007
#define ll long long

ll power(ll b, ll e)
{
    ll p = 1;
    while (e > 0)
    {
        if(e&1)
            p = (p*b)%mod;
        e = e>>1;
        b = (b * b)%mod;
    }
    return p;
}
int main()
{
    ll n,i,t,j,k,l,m;
    for(k=1,S1(t);k<=t;k++)
    {
        S1(n);
        printf("Case #%lld: ",k);
        if(n==0)
        {Pt("INSOMNIA");continue;}
        set<ll>s;
        for(i=1;s.size()<10&&i<80;i++)
        {
            m=n*i;
            while(m>0)
            {
                s.insert(m%10);
                m/=10;
            }
        }
        i--;
        P1(i*n);
    }
    return 0;
}

