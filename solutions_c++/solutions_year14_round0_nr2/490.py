/**À„∑®∑÷Œˆ£∫

*/
#include<bits/stdc++.h>
#define MAXN 105000
#define PI acos(-1.0)
#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,s,t) for(int i=s; i<=t; i++)
#define mem(a,b)  memset(a,b,sizeof(a))
#define show(x) { cerr<<">>>"<<#x<<" = "<<x<<endl; }
#define showtwo(x,y) { cerr<<">>>"<<#x<<"="<<x<<"  "<<#y<<" = "<<y<<endl; }
using namespace std;

int main()
{
    freopen("E:\\acm\\input.txt","r",stdin);
    freopen("E:\\acm\\output.txt","w",stdout);
    int T; cin>>T;
    FOR(cas,1,T)
    {
        double C,F,X;
        cin>>C>>F>>X;
        double ans = 0;

        double sp = 2;
        while(true)
        {
            if(X/sp <= (C/sp+X/(sp+F)))
            {
                ans += X/sp;
                break;
            }
            ans += C/sp;
            sp += F;
        }
        printf("Case #%d: ",cas);
        printf("%.7f\n",ans);
    }

}












