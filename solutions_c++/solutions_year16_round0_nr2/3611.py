#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char pancakes[101];

int solve()
{
    int length;
    int diff = 0;
    char compare;
    length = strlen(pancakes);

    compare = pancakes[0];

    for(int i = 1 ; i < length ; i++){
        if(compare != pancakes[i]){
            diff++;
            compare = pancakes[i];
        }
    }
    if(compare == '-'){
        diff++;
    }
    return diff;
}


int main()
{
    int count;
    FILE * fdin;
    FILE * fdout;

    fdin = fopen("B-large.in","r");
    fdout = fopen("B-large.out","w");

    fscanf(fdin,"%d",&count);

    for(int i = 1 ; i <= count ; i++ ){
        memset(pancakes,0,sizeof(pancakes));
        fscanf(fdin,"%s",pancakes);
        fprintf(fdout,"Case #%d: %d\n",i,solve());
    }

    fclose(fdin);
    fclose(fdout);

    return 0;
}
