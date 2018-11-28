#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
/*
int findAns(int **lawn,int n,int m)
{
    int sumN[n];
    int sumM[m];
    int sum;
    for(int i=0;i<n;i++)
    {
        sum=0;
        for(int j=0;j<m;j++)
        {
            sum=sum+lawn[i][j];
        }
        if(sum==n) sumN[i]++;
    }
    for(int j=0;j<m;j++)
    {
        sum=0;
        for(int i=0;i<n;i++)
        {
            sum=sum+lawn[i][j];
        }
        if(sum==m) sumM[j]++;
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(lawn[i][j]==1&&(sumN[i]==0||sumM[j]==0)) return 0;
        }
    }
    return 1;
}
*/

int main(int argc, char *argv[]) {

  FILE *in;
  in=fopen("B-small-attempt1.in","r");
  int t,n,m;
  fscanf(in,"%d",&t);
  //scanf("%d",&t);
  int ans[t];
  for(int x=0;x<t;x++)
  {
      fscanf(in,"%d",&n);
      fscanf(in,"%d",&m);
      //scanf("%d",&n);
      //scanf("%d",&m);
      int lawn[n][m];
      for(int j=0;j<n;j++)
      {
          for(int k=0;k<m;k++)
          {
              fscanf(in,"%d",&lawn[j][k]);
          }
      }
    //*  ---------
    int sumN[n];
    int sumM[m];
    int sum;
    for(int i=0;i<n;i++)
    {
        sum=0;
        for(int j=0;j<m;j++)
        {
            sum=sum+lawn[i][j];
        }
        sumN[i]=0;
        if(sum==m) sumN[i]=1;
        //printf("sumN[%d]=%d\n",i,sumN[i]);
    }
    for(int j=0;j<m;j++)
    {
        sum=0;
        for(int i=0;i<n;i++)
        {
            sum=sum+lawn[i][j];
        }
        sumM[j]=0;
        if(sum==n) sumM[j]=1;

        //printf("sumM[%d]=%d\n",j,sumM[j]);
    }
    ans[x]=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(lawn[i][j]==1&&(sumN[i]==0&&sumM[j]==0))
            {
                ans[x]= 1;
               // printf("anssumN[%d]=%d\n",i,sumN[i]);
              //  printf("anssumM[%d]=%d\n",j,sumM[j]);
                break;
            }
        }
        if(ans[x]==1) break;
    }

//    ans[i]=findAns(lawn,n,m);

  }
    FILE *out;
    out=fopen("outLawn1.txt","w");
  for(int x=0;x<t;x++)
  {
      if(ans[x]==0) fprintf(out,"Case #%d: YES\n",x+1);
    //printf("Case #%d: YES\n",x+1);
        else fprintf(out,"Case #%d: NO\n",x+1);
    //printf("Case #%d: NO\n",x+1);
    }
}
