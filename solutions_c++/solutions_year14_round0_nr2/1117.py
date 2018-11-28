#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
void solve(){
    double C,F,X;
    scanf("%lf %lf %lf",&C,&F,&X);
    double _rate=2.0;
    double _carry = 0 ;
    double answer = X/_rate;
    for(int i = 1 ; i<= 100000 ; ++ i ){
        _carry+= C/_rate;
        _rate+=F;
        answer=min(answer,_carry + X/_rate ) ;
    }
    printf("%.10lf\n",answer);
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i =  1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
