#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;

int main()
{
    int i,j,k,l,m,t,T,flag,flag2,counter,len;
    char A[101];
    FILE *fpi;
    FILE *fpo;
    fpi=fopen("B-large.in","r");
    fpo=fopen("revengeanslarge.txt","w");
    fscanf(fpi,"%d",&T);
    for(t=1;t<=T;t++)
    {
        counter=0;
        fscanf(fpi,"%s",A);
        len=strlen(A);
        if(len==1)
        {
            if(A[0]=='-')
                counter=1;
        }
        else
        {
            for(i=0;i<len-1;i++)
            {
                flag=0;
                if(A[len-1-i]!=A[len-2-i])
                {
                    flag=1;
                    counter++;
                }
                if(flag==1)
                {
                    for(j=0;j<len-i-1;j++)
                    {
                        if(A[j]=='+')
                            A[j]='-';
                        else
                            A[j]='+';
                    }
                }
            }
            if(A[0]!='+')
                counter++;
        }
        fprintf(fpo,"Case #%d: %d\n",t,counter);
    }
    return 0;
}
