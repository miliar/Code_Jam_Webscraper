#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main(){
    int T;
    int iii;
    FILE *ifp,*ofp;
    ifp=fopen("B-small-attempt0.in","r");
    ofp=fopen("small.txt","w");
    fscanf(ifp,"%d",&T);
    for(iii=1;iii<=T;iii++){
        double arr[1000]={0};
        double C,F,X,time;
        int n;
        time=0;
        fscanf(ifp,"%lf%lf%lf",&C,&F,&X);
        n=floor((X*F/C-2)/F);
        if(n<=0)
            n=0;
        printf("%d\n",n);
        for(int i=0;i<n;i++){
            time+=(C/(2+i*F));
        }
        time+=(X/(2+n*F));
        fprintf(ofp,"Case #%d: %.7lf",iii,time);
        if(iii!=T)
            fprintf(ofp,"\n");
    }
    return 0;
}
