#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

char* st(char a,bool over)
{
    char* t =(char*)malloc(40*sizeof(char));
    //char *t=new char[40];
    if(a!='.'){
        t[0]=a;t[1]=' ';t[2]='w';t[3]='o';t[4]='n';t[5]=0;}
    else if(over)
        t="Draw";
    else
        t="Game has not completed";
    return t;
}

int main()
{
    int N;
    FILE *in,*out;
    in=fopen("test.in","r");
    out=fopen("test.out","w");
    fscanf(in,"%d",&N);
    fgetc(in);
    for(int i=1;i<=N;i++)
    {
        bool over=true;
        char winner='.';
        char Matrix[5][5];
        for(int j=1;j<5;j++){
            for(int i1=1;i1<5;i1++)
            {
                if(!over)
                fscanf(in,"%c",&Matrix[j][i1]);
                else{char c=fgetc(in); Matrix[j][i1]=c;if(c=='.') over=false; }
            }
            while(fgetc(in)!='\n');
        }
        fgetc(in);

        for(int j=1;j<5;j++){
            if(Matrix[j][1]=='.')
                continue;
            else
            {
                int a;
                if(Matrix[j][1]!='T'){
                for(a=2;a<5;a++)
                {
                  //  printf("%d %d ",a,j);
                    if(Matrix[j][a]==Matrix[j][1] || Matrix[j][a]=='T')
                        continue;
                    else
                        break;
                }
                    if(a==5){winner=Matrix[j][1];};
                }
                else{
                    if(Matrix[j][2]!='.')
                    for(a=3;a<5;a++)
                        {
                    if(Matrix[j][a]==Matrix[j][2] || Matrix[j][a]=='T')
                        continue;
                    else
                        break;
                        }
                        if(a==5) {winner=Matrix[j][2];  }}
            }

        }
    //ALIOS
    if(winner=='.')
         for(int j=1;j<5;j++){
            if(Matrix[1][j]=='.')
                continue;
            else
            {
                int a;
                if(Matrix[j][1]!='T'){
                for(a=2;a<5;a++)
                {
                    if(Matrix[a][j]==Matrix[1][j] || Matrix[a][j]=='T')
                        continue;
                    else
                        break;
                }
                    if(a==5) {winner=Matrix[1][j] ; }
                }
                else{
                    if(Matrix[2][j]!='.')
                    for(a=3;a<5;a++)
                        {
                    if(Matrix[a][j]==Matrix[2][j] || Matrix[a][j]=='T')
                        continue;
                    else
                        break;
                        }
                        if(a==5) {winner=Matrix[2][j];}}
            }

        }
        if(winner=='.')
        {
            int a=0;
            if(Matrix[1][1]!='.'){
            if(Matrix[1][1]!='T'){
            for( a=2;a<5;a++)
            {
                if(Matrix[a][a]=='T') continue;
                if(Matrix[a][a]!=Matrix[1][1])
                    break;

            }
            if(a==5) {winner=Matrix[1][1]; }
            }
            else{
                if(Matrix[2][2]!='.')
               for( a=2;a<5;a++)
            {
                if(Matrix[a][a]=='T') continue;
                if(Matrix[a][a]!=Matrix[2][2])
                    break;

            }
            if(a==5) {winner=Matrix[2][2]; }
        } }
        }

         if(winner=='.')
        {
            int a=0;
            if(Matrix[1][4]!='.'){
            if(Matrix[1][4]!='T'){
            for( a=2;a<5;a++)
            {
                if(Matrix[a][5-a]=='T') continue;
                if(Matrix[a][5-a]==Matrix[1][4])
                    continue;
                else
                    break;

            }
            if(a==5) {winner=Matrix[1][4];}
            }
            else{
                    if(Matrix[2][4]!='.')
               for( a=2;a<5;a++)
            {
                if(Matrix[a][5-a]=='T') continue;
                if(Matrix[a][5-a]==Matrix[2][3])
                    continue;
                else
                    break;

            }
            if(a==5) {winner=Matrix[2][3]; ;}
        } }
        }
        char* state=st(winner,over);
        fprintf(out,"Case #%d: %s\n",i,state);
    }
    return 0;
}
