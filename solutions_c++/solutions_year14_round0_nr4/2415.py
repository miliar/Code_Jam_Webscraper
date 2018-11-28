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

double A[1000],B[1000];
int main()
{
    int T,n,t; si(t);T=t; while(t--)
    {
        cout<<"Case #"<<T-t<<": ";
        si(n);
        repi(i,n)cin>>A[i];
        repi(i,n)cin>>B[i];
        sort(A,A+n);
        sort(B,B+n);
        int i,j; 
        int c=0;
        i=j=n-1;
        while(1)
        {
            while(j>=0 && A[i]<B[j])
                j--;
            if(j<0)break;
            j--;i--;c++;
        }
        cout<<c<<" ";
        c=n;
        i=j=n-1;
        while(1)
        {
            while(j>=0 && B[i]<A[j])
                j--;
            if(j<0)break;
            j--;i--;c--;
        }
        cout<<c<<endl;
    }
    return 0;
}

