#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char str[1010];
char res[2020];

int startpos;
int endpos;

void solve1()
{
    startpos = 1001;
    endpos = 1001;
    res[startpos] = str[0];

    int length = strlen(str);

    for(int i = 1; i< length ; i++){
        if(str[i] >= res[startpos]){
            res[--startpos] = str[i];
        }else {
            res[++endpos] = str[i];
        }
    }
    res[endpos+1]='\0';
}


int main()
{
    int count,N,J;
    FILE * fdin;
    FILE * fdout;

    fdin = fopen("A-large.in","r");
    fdout = fopen("A-large.out","w");

    fscanf(fdin,"%d",&count);

    for(int i = 1 ; i <= count ; i++ ){
        fscanf(fdin,"%s",str);
        solve1();
        fprintf(fdout,"Case #%d: %s\n",i, res+startpos);
    }

    fclose(fdin);
    fclose(fdout);

    return 0;
}
