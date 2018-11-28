#include<stdio.h>
int main(){
    int i,T,X,R,C,res;
    scanf("%d",&T);
    for(i=0;i<T;i++){
        scanf("%d %d %d",&X,&R,&C);
        if(R>C){
            int tmp=C;
            C=R;
            R=tmp;
        }
        res=0;
        if(X==1) res=1;
        if(X==2){
            if(R==1){
                if(C==1) res=0;
                if(C==2) res=1;
                if(C==3) res=0;
                if(C==4) res=1;
            }
            if(R==2) res=1;
            if(R==3){
                if(C==3) res=0;
                if(C==4) res=1;
            }
            if(R==4) res=1;
        }
        if(X==3){
            if(R==1) res=0;
            if(R==2){
                if(C==3) res=1;
                else res=0;
            }
            if(R==3) res=1;
            if(R==4) res=0;
        }
        if(X==4){
            if(R==1) res=0;
            if(R==2) res=0;
            if(R==3){
                if(C==4) res=1;
                else res=0;
            }
            if(R==4) res=1;
        }
        if(res==0) printf("Case #%d: RICHARD\n",i+1);
        else printf("Case #%d: GABRIEL\n",i+1);
    }
}
