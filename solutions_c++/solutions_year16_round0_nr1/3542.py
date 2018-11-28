#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int compare[10]={1,2,4,8,16,32,64,128,256,512};
const int clear = 1|2|4|8|16|32|64|128|256|512;

int solve(int startnum )
{
    int mid ;
    int multi = 0;
    int checkflag = 0;

    if(startnum == 0 ){
        return -1;
    }

    while( checkflag != clear ){
        ++multi;
        mid = startnum * multi;
        while( mid > 0 ){
            checkflag |= compare[mid % 10];
            mid /= 10;
        }
    }
    return startnum * multi;
}


int main()
{
    int count = 1;
    int in,out;
    FILE * fdin;
    FILE * fdout;

    fdin = fopen("A-large.in","r");
    fdout = fopen("A-large.out","w");

    fscanf(fdin,"%d",&count);

    for(int i = 1 ; i <= count ; i++ ){
        fscanf(fdin,"%d",&in);
        out = solve(in);
        if(out == -1){
            fprintf(fdout,"Case #%d: INSOMNIA\n",i);
        }else{
            fprintf(fdout,"Case #%d: %d\n",i,out);
        }
    }

    fclose(fdin);
    fclose(fdout);

    return 0;
}
