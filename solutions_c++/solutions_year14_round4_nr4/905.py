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

string S[8];
int n,x;
int mx;
int cnt;
int cmp[8][8];

void fo(int l, int r)
{
    int i=0; 
    while(S[l][i]==S[r][i])i++;
    cmp[l][r]=i;
    cmp[r][l]=i;
}

void f(VI A)
{
    if(SZ(A)==x)
    {
        VI B[4];
        repi(i,x) B[A[i]].PB(i);
        int ans=0;
        repi(i,n)
        {
            if(B[i].empty())return;
            ans++; ans += SZ(S[B[i][0]]);
            for(int j=1; j<SZ(B[i]);j++)
            {
                ans += SZ(S[B[i][j]]);
                ans -= cmp[B[i][j]][B[i][j-1]];
            }
            if(ans==mx)cnt++; else if(ans>mx){mx=ans; cnt=1;}
        }
        return;
    }
    repi(i,n)
    {
        VI b = A; b.PB(i);
        f(b);
    }
}

int main()
{
    int t; si(t); int T = t; while(t--)
    {
        cin>>x>>n;
        repi(i,x)cin>>S[i]; 
        sort(S,S+x);
        SET(cmp,0);
        repi(i,x) for(int j=i+1; j<x;j++)fo(i,j);
        VI A;
        mx=0; cnt=0;
        f(A);
        cout<<"Case #"<<T-t<<": "<<mx<<" "<<cnt<<endl; 
    }
    return 0;
}

