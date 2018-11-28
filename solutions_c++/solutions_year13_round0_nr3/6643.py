#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sstream>
#include <math.h>
using namespace std;
bool ispalind(int A)
{
    string stra;
    ostringstream convert;
    convert << A;
    stra = convert.str();
   const char *s=stra.c_str(); //new char[stra.length()+1];
  //  strcpy(s)
    int maxi= stra.length()-1;
    int low=0;
    bool pali=true;
    while(low<maxi && pali==true)
    {
           // printf("%s %c %c\n",s,s[low],s[maxi]);
        if(s[low]!=s[maxi])
            pali= false;

        low++;
        maxi--;

    }
    return pali;
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
        int N,M;
        fscanf(in,"%d %d",&N,&M);
               // printf("aa");
        double Na=N;
        double Ma=M;
        Na=sqrt(Na);
        Ma=sqrt(Ma);
        int lown=(int)ceil(Na);
       int lowm=(int)floor(Ma);
   // printf("%d %d \n",lown ,lowm);
        int j=0;
        for(int k=lown;k<=lowm;k++)
        {
            if(ispalind(k)){
                {if(ispalind(k*k)){
                j++;
        }}}
        }


        fprintf(out,"Case #%d: %d\n",i,j);
    }
    return 0;
}
