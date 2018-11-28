#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int Nstring[33];

long long getFactor(long long input)
{
    if( input < 2 ) return input;
    if( input <  4 ) return -1;

    if( input% 2 == 0 ) return 2;

    for(int i = 3 ; (i*i <= input)&&(i<50) ; i+=2 ){
        if( (input % i) == 0 ){
            return i;
        }
    }
    return -1;
}

void solve(FILE* fdout, int numsize, int answercount)
{
    int count;
    long long point,mid;
    long long factorArr[10];
    int i, j;
    memset(Nstring,0,sizeof(int)*numsize);
    Nstring[0] = 1;
    Nstring[numsize-1] = 1;

    while( answercount > 0 ){
        // create new number
        for(i = 1 ; i < (numsize-1) ; i++){
            if(Nstring[i] == 0){
                Nstring[i] = 1;
                break;
            }else{
                Nstring[i] = 0;
            }
        }
        if(numsize - 1 == i){
            printf("error\n");
            break;
        }
        // make
        for( i = 2 ; i <= 10; i++ ){
            mid = 1;
            point = 1;
            for( j = 1 ; j < numsize ; j++){
                point *= i;
                if( Nstring[j] == 1){
                    mid += point;
                }
            }

            // check mid has factor
            factorArr[i] = getFactor(mid);
            if(factorArr[i] == -1){
                break;
            }
        }
        if(i == 11){
            fprintf(fdout,"%lld",mid);

            for( j = 2 ; j < 11 ; j++ ){
                fprintf(fdout," %lld",factorArr[j]);
            }
            fprintf(fdout,"\n");
            --answercount;
        }
    }
}


int main()
{
    int count,N,J;
    FILE * fdin;
    FILE * fdout;

    fdin = fopen("C-small-attempt0.in","r");
    fdout = fopen("C-small.out","w");

    fscanf(fdin,"%d",&count);

    for(int i = 1 ; i <= count ; i++ ){
        fscanf(fdin,"%d %d",&N,&J);
        fprintf(fdout,"Case #%d:\n",i);
        solve(fdout,N,J);
    }

    fclose(fdin);
    fclose(fdout);

    return 0;
}
