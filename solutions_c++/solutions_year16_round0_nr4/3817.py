#include<cstdio>
#include<iostream>
using namespace std;
int main(){
    FILE *rf,*wf;
    rf=fopen("A.txt","r");
    wf=fopen("Aa.txt","w");
    int t,k,c,s;
    fscanf(rf,"%d",&t);
    for(int i=0;i<t;i++){

        fscanf(rf,"%d%d%d",&k,&c,&s);
        fprintf(wf,"Case #%d: ",i+1);
        for(int j=1;j<=k;j++)
            fprintf(wf,"%d ",j);
        fprintf(wf,"\n");
    }
    return 0;
}
