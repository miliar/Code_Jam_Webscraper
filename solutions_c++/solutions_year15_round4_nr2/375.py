#include<bits/stdc++.h>
#define DB double
using namespace std;
const DB eps=1e-9 ;
const int maxn=100+10 ;

DB r[maxn],c[maxn] ;
main()
{
    if(fopen("B.in","r"))
        freopen("B.in","r",stdin) ,
        freopen("B.out","w",stdout) ;
    int T,tc=0 ; scanf("%d",&T) ;
    while(T--)
    {
        printf("Case #%d: ",++tc) ;
        DB V,X ;
        int n ; scanf("%d%lf%lf",&n,&V,&X) ;
        for(int i=1;i<=n;i++) scanf("%lf%lf",&r[i],&c[i]) ;
        if(n==1)
        {
            if(fabs(c[1]-X)>eps) printf("IMPOSSIBLE\n") ;
            else printf("%.10f\n",V/r[1]) ;
        }
        if(n==2)
        {
            if(c[1]>c[2]) swap(c[1],c[2]) , swap(r[1],r[2]) ;
            if(X-c[2]>eps || c[1]-X>eps)
                {printf("IMPOSSIBLE\n") ; continue ;}
            if(fabs(c[1]-c[2])<eps) printf("%.10f\n",V/(r[1]+r[2])) ;
            else if(fabs(X-c[2])<eps) printf("%.10f\n",V/r[2]) ;
            else if(fabs(X-c[1])<eps) printf("%.10f\n",V/r[1]) ;
            else
            {
                DB rat=(c[2]-X)/(X-c[1]) ;
                printf("%.10f\n",max( V*rat/(1+rat)/r[1] , V/(1+rat)/r[2] )) ;
            }
        }
    }
}
