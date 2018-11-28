#include <stdio.h>
#include <math.h>
using namespace std;

int main() {

    //freopen("D-small-attempt1.in","r",stdin);
    //freopen("D-small-attempt1.out","w",stdout);
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);

    int T,X,R,C,Rm;
    //X=3;
    //printf("%d", X%2);

    while(scanf("%d",&T)==1 && T<=100)
    {
        for(int t=1;t<=T;t++){

        scanf("%d %d %d", &X, &R, &C);
        Rm = (R*C);
        /*
            if(Rm>=X){
                    if((Rm%X)==0){
                        if(X==Rm)
                            printf("Case #%d: RICHARD\n", t);
                        else
                            printf("Case #%d: GABRIEL\n", t);
                    }
                    else
                        printf("Case #%d: RICHARD\n", t);
            }
            else
                printf("Case #%d: RICHARD\n", t);
        }
        */
        if((X>R) && (X>C)){
            printf("Case #%d: RICHARD\n", t);
        }
        else if(X==1){
            printf("Case #%d: GABRIEL\n", t);
        }
        else if(X==2){
            if(Rm%X==0)
                printf("Case #%d: GABRIEL\n", t);
            else
            //if(Rm==6 || Rm==9)
                printf("Case #%d: RICHARD\n", t);
            //else
              //  printf("Case #%d: GABRIEL\n", t);
        }
        else if(X==3){
            if(Rm==6 || Rm==9 || Rm==12)
                printf("Case #%d: GABRIEL\n", t);
            else
                printf("Case #%d: RICHARD\n", t);
        }
        else if(X==4){
            if(Rm==12 || Rm==16)
                printf("Case #%d: GABRIEL\n", t);
            else
                printf("Case #%d: RICHARD\n", t);
        }
    }
    }

    return 0;
}
