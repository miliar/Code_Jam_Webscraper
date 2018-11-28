using namespace std;
#include<bits/stdc++.h>

#define BG begin()
#define ED end()
#define st first
#define nd second
#define PB push_back
#define PF push_front
#define FOR(i,a,b) for (int i=a;i<b;i++)
#define FORE(i,a,b) for (int i=a;i<=b;i++)
#define FORD(i,a,b) for (long long i=a;i>=b; i--)
#define ri(n)({\
    int neg=0;\
    n=0;\
    char ch;\
    for(ch=getchar(); ch<'0' || ch>'9'; ch=getchar()) if (ch=='-') neg=1-neg;\
    n=ch-48;\
    for(ch=getchar(); ch>='0' && ch<='9'; ch=getchar()) n=(n<<3)+(n<<1)+ch-48;\
    if (neg) n=-n;\
})

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> II;
typedef pair<ll,ll> LL;
const ll INF=1000000000+7;
const double esp=1e-13;
const double pi=3.141592653589;

ll canhai(ll n)
{
    ll fi,la,mid;
    fi=0;
    la=n+1;
    while (fi+1<la)
    {
        mid=fi/2+la/2;
        if (fi%2 && la%2) mid++;
        if (mid>n/mid) la=mid;
        else fi=mid;
    }
    return fi;
}

int test,a[1000+10],ans,n,dem,tinh;

void xuli()
{
    dem++;
    cin >> n;
    FORE(i,1,n) cin >> a[i];
    sort(a+1,a+n+1);
    ans=INF;
    FORE(i,1,a[n])
    {
        tinh=0;
        FORD(j,n,1)
        if (a[j]>=i) tinh+=(a[j]-i)/i+((a[j]-i)%i!=0);
        else break;
        ans=min(ans,tinh+i);
    }
    cout << "Case #" << dem << ": " << ans << "\n";
}

int main()
{
   // freopen("codeforces.inp", "r", stdin);
   // freopen("6224486.out", "w", stdout);
    dem=0;
    cin >> test;
    while (test--) xuli();
}

