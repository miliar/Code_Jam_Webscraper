#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int arrsize;
int hash[2502];

void input(FILE* fdin )
{
    int temp;

    fscanf(fdin,"%d",&arrsize);

    memset(hash,0,sizeof(hash));

    for(int i = 0 ; i < (arrsize*2 -1) ; i++ ){
        for(int j = 0 ; j<arrsize ; j++){
            fscanf(fdin,"%d",&temp);
            hash[temp]++;
        }
    }
}
void solve1(FILE* fdout )
{
    int prtcnt = 0;
    for(int i = 1; (i< 2501) && (prtcnt < arrsize) ; i++ ){
        if((hash[i]%2) != 0){
            fprintf(fdout," %d",i);
            prtcnt++;
        }
    }
    fprintf(fdout,"\n");
}


int main()
{
    int count,N,J;
    FILE * fdin;
    FILE * fdout;

    fdin = fopen("B-large.in","r");
    fdout = fopen("B-large.out","w");

    fscanf(fdin,"%d",&count);

    for(int i = 1 ; i <= count ; i++ ){
        input(fdin);
        fprintf(fdout,"Case #%d:",i);
        solve1(fdout);
    }

    fclose(fdin);
    fclose(fdout);

    return 0;
}
