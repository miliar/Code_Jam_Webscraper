// karanaggarwal
#include<bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define CLR(a) a.clear()
#define SET(a,b) memset(a,b,sizeof(a))
#define LET(x,a) __typeof(a) x(a)
#define TR(v,it) for( LET(it,v.begin()) ; it != v.end() ; it++)
#define FORi(i,a,b) for(LET(i,a) ; i<b; i++)
#define repi(i,n) FORi(i,(__typeof(n))0,n)
#define FOR(i,a,b) for(i=a ; i<b; i++)
#define rep(i,n) FOR(i,0,n)
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define pi(n) printf("%d",n)
#define piw(n) printf("%d ",n)
#define pin(n) printf("%d\n",n)
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< PII > VPII;
LL power(LL a, LL p, LL mod)
{LL ret = 1;while(p){if(p&1)ret = (ret*a)%mod;a=(a*a)%mod;p/=2;}return ret;}
int B[10];
int n;
int og[10];

int f(VI A) // A --> B
{
    int ret=0;
    for(int i=0; i<n; i++)
    {
        int j=i;
        while(A[j]!=B[i])j++;
        for(int k=j; k>i;k--)
        {
            A[k]=A[k-1];
            ret++;
        }
        A[i]=B[i];
    }
    return ret;
}

int main()
{
    int t; si(t); int T = t; while(t--)
    {
        cin>>n;
        repi(i,n)si(og[i]);
        VI A; repi(i,n)A.PB(og[i]); 
        VI ts = A;
        sort(A.begin(),A.end());
        int ans=100000;
        // A sorted vector      og is og array     B is to convert
        repi(i,1<<(n-1))
        {
            int s=0; int l = n-1;
            repi(j,n-1)
            {
                if((i>>j)&1)
                    B[l--] = A[j];
                else
                    B[s++] = A[j];
            }
            B[s] = A[n-1];
            ans = min(ans,f(ts));
        }
        cout<<"Case #"<<T-t<<": "<< ans<<endl;
    }
    return 0;
}

