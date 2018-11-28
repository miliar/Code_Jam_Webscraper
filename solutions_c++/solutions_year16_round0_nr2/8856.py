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
char s[102];
int main()
{
    ll n,i,t,j,k,l,m,f;
    for(k=1,S1(t);k<=t;k++)
    {
        f=0;
        St(s);
        n=strlen(s);
        printf("Case #%lld: ",k);
        for(i=n-1;i>=0;i--)
        {
            l=(s[i]=='+')?1:0;
            if((l+f%2)%2==0)
            {
                f++;
            }
        }
        P1(f);
    }
    return 0;
}

