#include<stdio.h>
#include<string.h>
#include<stdlib.h>

FILE * fdout;

void solve(int orgsize, int comp, int cleaner )
{
    int startpos;

    if(comp == 1){
        if(cleaner < orgsize ){
           fprintf(fdout,"IMPOSSIBLE\n");
            return;
        }
        startpos = 1;
    }else{
        if(cleaner < (orgsize-1) ){
            fprintf(fdout,"IMPOSSIBLE\n");
            return;
        }
        startpos = 2;
    }

    for(int i = startpos ; i < orgsize ; i++){
        fprintf(fdout,"%d ",i);
    }
    fprintf(fdout,"%d\n",orgsize);
}


int main()
{
    int count,K,C,S;
    FILE * fdin;

    fdin = fopen("D-small-attempt0.in","r");
    fdout = fopen("D-small.out","w");

    fscanf(fdin,"%d",&count);

    for(int i = 1 ; i <= count ; i++ ){
        fscanf(fdin,"%d %d %d",&K,&C,&S);
        fprintf(fdout,"Case #%d: ",i);
        solve(K,C,S);
    }

    fclose(fdin);
    fclose(fdout);

    return 0;
}
