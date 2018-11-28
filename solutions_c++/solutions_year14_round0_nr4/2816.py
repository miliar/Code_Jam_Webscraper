#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int cmp(const void* pa, const void* pb){
    double a=*(double *)pa;
    double b=*(double *)pb;
    if (a<b)
        return -1;
    else if(a>b)
        return 1;
    return 0;
}
int main(){
    int T;
    int iii;
    FILE *ifp,*ofp;
    ifp=fopen("D-large.in","r");
    ofp=fopen("out.txt","w");
    fscanf(ifp,"%d",&T);
    for(iii=1;iii<=T;iii++){
        double naomi[2000],ken[2000];
        int n,y,z;
        fscanf(ifp,"%d",&n);
        for(int i=0;i<n;i++)
            fscanf(ifp,"%lf",naomi+i);
        for(int i=0;i<n;i++)
            fscanf(ifp,"%lf",ken+i);
        y=z=0;
        qsort(naomi,n,sizeof(double),cmp);
        qsort(ken,n,sizeof(double),cmp);
        for(int i=0;i<n-1;i++)
            if(naomi[i]==naomi[i+1])
                printf("FFFFFFFFFFFFFFFFFFF\n");
        int i,j;
        i=j=0;
        while(i<n&&j<n){
            if(ken[i]>naomi[j]){
                i++;j++;z++;
            }
            else{
                i++;
            }
        }
        i=j=0;
        z=n-z;
        while(i<n&&j<n){
            if(naomi[i]>ken[j]){
                i++;j++;y++;
            }
            else{
                i++;
            }
        }
        fprintf(ofp,"Case #%d: %d %d",iii,y,z);
        if(iii!=T)
            fprintf(ofp,"\n");
    }
    return 0;
}
