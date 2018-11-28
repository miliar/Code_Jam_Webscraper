#include <stdio.h>

int main(){
    int TT;
    scanf("%d",&TT);
    for( int tt=0; tt<TT; tt++ ){
        double C,F,X;
        scanf("%lf %lf %lf",&C,&F,&X);
        double s = 0;
        double md=X/2;
        for( int i=0; i<1000000; i++ ){
            double d = s+X/(2+i*F);
            if(d<md) md = d;
            s += C/(2+i*F);
        }
        printf("Case #%d: %.6f\n",tt+1,md);
    }
    return 0;
}
