#include <bits/stdc++.h>

#define FI(ii,aa,bb) for(ll ii=aa;ii<=bb;ii++)
#define F(ii,aa,bb) for(ll ii=aa;ii<bb;ii++)
#define TF(ii,aa,bb) for(ll ii=aa;ii>=bb;ii--)
#define mp make_pair
#define pii pair<ll,ll>
#define st first
#define nd second
#define pb push_back
#define pdd pair<double,double>
#define ll long long
#define inf (ll_MAX)

using namespace std;

double goal,cost,ex;

int main()
{

     // freopen("in21.in","r",stdin);
     // freopen("out21.out","w",stdout);
      int T;
      scanf("%d",&T);
      FI(t,1,T){
            scanf("%lf %lf %lf",&cost,&ex,&goal);
            double money=0,ans=0,pro=2.0;
            if(goal<=cost){
                  printf("Case #%d: ",t);
                  printf("%.7lf\n",goal/2.0);
                  continue;
            }
            while(money<goal){
                  ans+=(cost-money)/pro;
                  money=cost;
                  if((goal-money)/pro > goal/(pro+ex)){
                        pro+=ex;
                        money-=cost;
                  }
                  else{
                        ans+=(goal-money)/pro;
                        money=goal;
                  }
            }
            printf("Case #%d: ",t);
            printf("%.7lf\n",ans);
      }
      return 0;
}
