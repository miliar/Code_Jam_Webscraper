#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int digit(int n, int d) {
    int val[9];
    for(int i=0;i<=100;i++)
    {
        val[i]=pow(10,i);
    }
  return (n / val[d]) % 10;
}

int findD(int num)
{
    for(int i=1;i<=100;i++)
    {
        if(num<pow(10,i)) return i;
    }
    return 100;
}

int isPalindrome(int num,int d)
{
    int number[d];
    for(int i=0;i<d;i++)
    {
        number[i]=digit(num,i);
    }
    int fid=0,bid=d-1;
    while(fid<=bid)
    {
        if(number[fid]!=number[bid]) return 0;
        fid++;
        bid--;
    }
    return 1;
}

int main(int argc, char *argv[]) {
  FILE *in;
  in=fopen("C-small-attempt1.in","r");
  int n,a,b;
  fscanf(in,"%d",&n);
  //scanf("%d",&n);
  int sum[n];
  for(int i=0;i<n;i++)
  {
      sum[i]=0;
      fscanf(in,"%d",&a);
      fscanf(in,"%d",&b);
      //scanf("%d",&a);
      //scanf("%d",&b);
      int sqrtA = sqrt(a);
      int sqrtB = sqrt(b);
      if(isPalindrome(sqrtA,findD(sqrtA))==1&&sqrtA*sqrtA>=a&&sqrtA*sqrtA<=b) sum[i]=sum[i]++;
      //printf("%d\n",sum[i]);
      for(int j=sqrtA+1;j<=sqrtB;j++)
      {
          int power=j*j;
          if(isPalindrome(j,findD(j))==1&&power>=a&&power<=b)
          {
              if(isPalindrome(power,findD(power))==1)
              {
                  sum[i]++;
               // printf("numP=%d\n",j);
              }
          }
          //printf("%d\n",sum[i]);
          //printf("%d\n",isPalindrome(j,findD(j))==1&&power>=a&&power<=b);
      }
  }
    FILE *out;
    out=fopen("outFS1.txt","w");
  for(int q=0;q<n;q++)
  {
      fprintf(out,"Case #%d: %d\n",q+1,sum[q]);
    //printf("Case #%d: %d\n",q+1,sum[q]);
    }
}
