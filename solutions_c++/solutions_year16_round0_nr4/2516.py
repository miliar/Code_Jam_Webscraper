#include<cstdio>

using namespace std;

int main(void){
    FILE *in,*out;
    int i,t,j,k,c,s;

    in=fopen("input.txt","r");
    out=fopen("output.txt","w");

    fscanf(in,"%d",&t);

    for(i=1;i<=t;i++){
        fscanf(in,"%d %d %d",&k,&c,&s);
        fprintf(out,"Case #%d:",i);
        for(j=1;j<=k;j++)fprintf(out," %d",j);
        fprintf(out,"\n");
    }



    return 0;
}
