#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char str[2001];
int Alpha[26]={0};
char * numStr[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int   numCheck[10][6];
int  checkArr[10]={0,6,8,2,4,1,5,3,7,9};
int  countArr[10];

void init()
{
    int length;
    int i ,j;
    for( j = 0 ; j<10 ; j++){

        length = strlen(numStr[j]);

        for( i = 0 ; i<length ; i++)
        {
            numCheck[j][i] = numStr[j][i]- 'A';
        }
        numCheck[j][i] = -1;
    }
}
void input ()
{
    memset(Alpha,0,sizeof(Alpha));

    int length = strlen(str);

    for(int i = 0 ; i < length ; i++)
    {
        Alpha[ str[i]-'A']++;
    }
}

int check(int * checknum)
{
    int count = 0;

    while(true){
        for(int i = 0 ; checknum[i] >= 0 ; i++)
        {
            if( Alpha[ checknum[i] ] > 0 ){
                Alpha[ checknum[i] ] --;
            }
            else{
                for(int j = 0 ; j<i ; j++)
                {
                   Alpha[ checknum[j] ] ++;
                }
                return count;
            }
        }
        count++;
    }

    return count;
}

void solve(FILE* fdout)
{
    int count;
    for(int i = 0 ; i < 10 ; i++)
    {
        countArr[checkArr[i]] = check(numCheck[checkArr[i]]);
    }
    for(int i = 0 ; i<10 ; i++){
        while(--countArr[i] >= 0 )
        {
            fprintf(fdout,"%d", i );
        }
    }
}


int main()
{
    int count,N,J;
    FILE * fdin;
    FILE * fdout;

    fdin = fopen("A-large.in.txt","r");
    fdout = fopen("A-large.out","w");

    fscanf(fdin,"%d",&count);

    init();

    for(int i = 1 ; i <= count ; i++ ){
        fscanf(fdin,"%s",str);
        input();
        fprintf(fdout,"Case #%d: ",i );
        solve(fdout);
        fprintf(fdout,"\n" );
    }

    fclose(fdin);
    fclose(fdout);

    return 0;
}
