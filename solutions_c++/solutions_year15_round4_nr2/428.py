#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <cstdlib>
#include <vector>

using namespace std;

int n ;
double X,V;

double C[2] , R[2] ;

int main(){

    freopen("input.txt" , "r" , stdin) ;
    freopen("output.txt" , "w" , stdout) ;
    int _ ; scanf("%d",&_);
    for (int cas = 1 ; cas <= _ ; cas++){
        scanf("%d" , &n) ;
        scanf("%lf%lf" , &V , &X) ;
        for (int i = 0 ; i < n ; i++)
            scanf("%lf%lf" , &R[i] , &C[i]) ;

        printf("Case #%d: ",cas) ;
        if (n == 1){
            if (C[0] != X) printf("IMPOSSIBLE\n") ;
            else printf("%.12f\n" , V / R[0]) ;
        }else{
            if (max(C[0],C[1]) < X || min(C[0],C[1]) > X) printf("IMPOSSIBLE\n") ;
            else{

                if (C[0] == C[1]){
                    printf("%.12f\n" , V / (R[0] + R[1])) ;
                }else{
                    X *= V ;
                    double v2 = (X - V * C[0]) / (C[1] - C[0]) ;
                    double v1 = V - v2 ;
                    printf("%.12f\n" , max(v2 / R[1] , v1 / R[0])) ;
                }
            }
        }
        //cout << 207221.843687375 * 0.0001 + 0.092778156 * 100.0 << endl ;
    }
    return 0 ;

}
