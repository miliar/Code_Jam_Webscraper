/// Allah, enlarge my knowledge, as I can enlighten your creation.
/*Minhaz Ahmed Syrus (msyrus)*/

#include <iostream>

using namespace std;

int main(){
    freopen("BH.in","r",stdin);
    freopen("BH.txt","w",stdout);
    int T, N;
    double C, F, X, res;
    scanf(" %d",&T);
    for(int cas=0; cas<T; ){
        scanf(" %lf %lf %lf",&C,&F,&X);
        res=0;
        double t=2;
        while((X/(t+F))<((X-C)/t)){
            res+=(C/t);
            t+=F;
        }
        res+=(X/t);
        printf("Case #%d: %0.9lf\n",++cas,res);
    }
    return 0;
}
