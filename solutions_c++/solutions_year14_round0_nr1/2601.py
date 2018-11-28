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


int main()
{
    int t; si(t); int T; T=t;while(t--)
    {
        cout<<"Case #"<<T-t<<": ";
        int fre[17]={};
        int A[4][4];
        int r; 
        si(r); 
        repi(i,4)repi(j,4)si(A[i][j]);
        repi(i,4) fre[A[r-1][i]]++;
        si(r); 
        repi(i,4)repi(j,4)si(A[i][j]);
        repi(i,4) fre[A[r-1][i]]++;
        VI tp;
        repi(i,17) if(fre[i]>1)tp.PB(i);
        int n = SZ(tp);
        if(n==0)
            cout<<"Volunteer cheated!\n";
        if(n==1)
            cout<<tp[0]<<endl;
        if(n>1)
            cout<<"Bad magician!\n";
    }
    return 0;

}

