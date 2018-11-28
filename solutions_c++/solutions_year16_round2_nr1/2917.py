#include <iostream>
#include <algorithm>
#include <limits>
#include <iterator>
#include <functional>
#include <string.h>
#include <stdio.h>

using namespace std;

int main()
{
    FILE *fpi,*fpo;
    fpi=fopen("A-large.in","r");
    fpo=fopen("write1.out","w");
    int t,T,A[26],L,i,j,k,*ans,ansind,d,c,e,swaps;
    char *S;
    fscanf(fpi,"%d",&T);
    //printf("%d",T);
    for(t=1;t<=T;t++)
    {

        ansind=0;
        ans=(int*)calloc(1000,sizeof(int));
        S=(char*)calloc(3000,sizeof(char));
        for(i=0;i<26;i++)
            A[i]=0;
        fscanf(fpi,"%s",S);
        L=strlen(S);
        for(i=0;i<L;i++){
            A[S[i]-65]++;
        }
            if(A[25]>0)
            {
                d=A[25];
                A[4]-=d;
                A[17]-=d;
                A[14]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=0;
            }
            if(A[20]>0)
            {
                d=A[20];
                A[5]-=d;
                A[14]-=d;
                A[17]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=4;
            }
            if(A[23]>0)
            {
                d=A[23];
                A[18]-=d;
                A[8]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=6;
            }
            if(A[6]>0)
            {
                d=A[6];
                A[4]-=d;
                A[8]-=d;
                A[7]-=d;
                A[19]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=8;
            }
            if(A[18]>0)
            {
                d=A[18];
                A[4]-=(2*d);
                A[21]-=d;
                A[13]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=7;
            }
            if(A[5]>0)
            {
                d=A[5];
                A[8]-=d;
                A[21]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=5;
            }
            if(A[7]>0)
            {
                d=A[7];
                A[19]-=d;
                A[17]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=3;
            }
            if(A[19]>0)
            {
                d=A[19];
                A[14]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=2;
            }
            if(A[14]>0)
            {
                d=A[14];
                A[13]-=d;
                for(j=0;j<d;j++)
                    ans[ansind++]=1;
            }
            if(A[13]>0)
            {
                d=A[13]/2;
                for(j=0;j<d;j++)
                    ans[ansind++]=9;
            }
            for (c = 0 ; c < ( ansind - 1 ); c++)
              {
                for (e = 0 ; e < ansind - c - 1; e++)
                {
                  if (ans[e] > ans[e+1]) /* For decreasing order use < */
                  {
                    swaps       = ans[e];
                    ans[e]   = ans[e+1];
                    ans[e+1] = swaps;
                  }
                }
              }
        //      printf("%d",ans[i]);
        fprintf(fpo,"Case #%d: ",t);
        for(i=0;i<ansind;i++)
            fprintf(fpo,"%d",ans[i]);
        fprintf(fpo,"\n");
        free(ans);
        free(S);
    }

}
