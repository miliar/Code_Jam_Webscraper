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
    int T,t; si(t);T=t;  while(t--)
    {
        cout<<"Case #"<<T-t<<": ";
        double X,C,R,F;
        R = 2;
        cin>>C>>F>>X;
        double t1 = X/R;
        double t=0,t2 = 0;
        double ans = t1;
//        double  K = (F*(C-X) - 2*C )/(F*C);
//        K = -1*K;
//        int k=0;
        while(1)
        {
            t += C/R; R+=F;
            t2 = t + X/R;
            ans = min(ans,t2);
//            k++;
            if(t2>t1)break;
            t1 = t2;
        }
        printf("%.7lf\n",ans);
//        cout<<K<<" "<<k<<endl;
    }
    return 0;
}

