#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{
    FILE *infile  = fopen("test.in", "r");
    FILE *outfile = fopen("out.txt", "w");

    int m;
    fscanf(infile,"%d",&m);
    for(int z=1;z<=m;z++)
    {
        int temp,turn=0,pos,n,happy=0;
        char input[11];
        fscanf(infile,"%s",&input);
        n=strlen(input);
       for(int i=0;i<n;i++)
       {
           if(input[i]=='+')happy++;
       }
       while(happy!=n)
        {
            if(happy==0)
            {
                turn++;
                break;
            }
            if(input[0]=='+')
            {
                turn++;
                for(int i=0;i<n;i++)
                {
                    if(input[i]=='-')break;
                    input[i]='-';
                    happy--;
                }

            }
            if(input[0]=='-')
            {
                turn++;
                for(int i=0;i<n;i++)
                {
                    if(input[i]=='+')break;
                    input[i]='+';
                    happy++;
                }

            }
        }
        fprintf(outfile,"Case #%d: %d\n",z,turn);
        //cout<<"Case #"<<z<<": "<<turn<<endl;
    }
}

