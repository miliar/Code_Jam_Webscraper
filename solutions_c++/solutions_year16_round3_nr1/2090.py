#include<stdio.h>
#include<string.h>
#include<stdlib.h>

FILE * fdin;
FILE * fdout;

int partcnt;
int parts[27];
int allmembers;
int excep;
int excepidx[2];

void input()
{
    fscanf(fdin,"%d", &partcnt );
    allmembers = 0;
    for(int i = 0 ; i < partcnt ; i++){
        fscanf(fdin,"%d", parts + i );
        allmembers += parts[i];
    }
}

void findMax()
{
    int max    = 0;
    int maxidx = -1;
    excepidx[0] = -1;
    excepidx[1] = -1;
    for(int i = 0 ; i < partcnt ; i++){
        if( max > parts[i])
        {
            continue;
        }
        if( max < parts[i] ){
            max = parts[i];
            excepidx[0] = i;
            excepidx[1] = -1;
        } else if( max > 0 ){
            excepidx[1] = i;
        }
    }
    if((excepidx[0]>=0) ||
       (excepidx[1]>=0))
    { 
        fprintf(fdout," ");
    }

    if((allmembers == 3)&&
       (excepidx[0]>=0) &&
       (excepidx[1]>=0))
    {
        if(parts[excepidx[0]] > parts[excepidx[1]])
        {
            excepidx[1] = -1;
        } else
        {
            excepidx[0] = -1;
        }
    }

    if(excepidx[0]>=0){
        fprintf(fdout,"%c",excepidx[0]+'A');
        --allmembers;
        --parts[excepidx[0]];
    }
    if(excepidx[1]>=0){
        fprintf(fdout,"%c",excepidx[1]+'A');
        --allmembers;
        --parts[excepidx[1]];
    }
}


void solve()
{
    while( allmembers > 0 )
    {
        findMax();
    }
    fprintf(fdout,"\n");
}


int main ()
{
    int count;
    fdin  = fopen("A-large.in","r");
    fdout = fopen("A-large.out","w");

    fscanf(fdin,"%d",&count);

    for(int i = 1 ; i <= count ; i++){
        input();
        fprintf(fdout,"Case #%d:",i);
        solve();
    }
    fclose(fdin);
    fclose(fdout);

    return 0;
}
