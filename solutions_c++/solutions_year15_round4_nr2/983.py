#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;

int n ;
double X,V;
double C[2],R[2] ;

int main(){

    freopen("B-small-attempt3.in" , "r" , stdin) ;
    freopen("B-small.out" , "w" , stdout) ;
    int T;
    int cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%lf%lf",&n,&V,&X);
        for (int i = 0 ; i < n ; i++)
        scanf("%lf%lf",&R[i],&C[i]) ;
        if (n == 1)
        {
            if (C[0] != X) printf("Case #%d: IMPOSSIBLE\n",++cas);
            else printf("Case #%d: %.12f\n",++cas,V/R[0]) ;
        }
        else
        {
            if (max(C[0],C[1]) < X || min(C[0],C[1]) > X) printf("Case #%d: IMPOSSIBLE\n",++cas) ;
            else
            {
                if (C[0] == C[1]){
                    printf("Case #%d: %.12f\n",++cas,V/(R[0]+R[1])) ;
                }else
                {
                    X *= V ;
                    double v2 = (X - V*C[0]) / (C[1]-C[0]) ;
                    double v1 = V - v2 ;
                    printf("Case #%d: %.12f\n",++cas,max(v2/R[1], v1/R[0])) ;
                }
            }
        }
    }
    return 0 ;

}
