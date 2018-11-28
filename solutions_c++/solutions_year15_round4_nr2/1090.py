#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#define ll long long
#define db double
using namespace std;

const double eps=1e-8;

int t,n,m;
db V,Tp;
db v[110],tp[110];

int main()
{
#ifdef Haha
    freopen("B-small-attempt4.in", "r", stdin);
    freopen("A-small-attempt0.out","w",stdout);
#endif // Haha
    scanf("%d",&t);
    for(int cas=1; cas<=t; cas++)
    {
        scanf("%d%lf%lf",&n,&V,&Tp);
        printf("Case #%d: ",cas);
        for(int i=0; i<n; i++) scanf("%lf%lf",&v[i],&tp[i]);
        if(n==1)
        {
            if(fabs(tp[0]-Tp)<eps) printf("%.8f\n",V/v[0]);
            else printf("IMPOSSIBLE\n");
        }
        else
        {
            if((tp[0]>Tp+eps&&tp[1]>Tp+eps)||(tp[0]<Tp-eps&&tp[1]<Tp-eps)) printf("IMPOSSIBLE\n");
            else if(fabs(tp[0]-tp[1])<eps)
            {
                printf("%.8f\n",V/(v[0]+v[1]));
            }
            else
            {
                db res=V*(Tp-tp[1])/(tp[0]-tp[1]);
                printf("%.8f\n",max(res/v[0],(V-res)/v[1]));
            }
        }
    }
    return 0;
}
