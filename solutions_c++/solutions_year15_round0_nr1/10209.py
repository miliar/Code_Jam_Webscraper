#include <iostream>
#include <stdio.h>
using namespace std;
int in[7];
int main()
{
int max;

int inpt, temp, factor;
int t,j;
int tc;
int k;
int stand, f;
freopen ("A-small-attempt1.in","r",stdin);
freopen ("output-a.txt","w",stdout);
scanf ("%d",&t);
//printf("%d\n", t);
for (tc = 1; tc <= t; tc++)
{
 scanf ("%d",&max);
 //printf("%d\n", max);
 scanf("%d", &inpt);
 //printf("\n++++%d\n", inpt);
 factor = 1;
 temp=inpt;
  while(temp){
      temp=temp/10;
      factor = factor*10;
  }
  k=0;
  while(factor>1){
      factor = factor/10;
      in[k++] = inpt/factor;

      inpt = inpt % factor;
  }
 // printf("\n%d", max);
// printf("%c", 'h');
 // printf("%d\n", k);
  inpt = k;
   for(temp=0;temp<k;temp++)
//  printf("%d", in[temp]);
  for(temp=k;temp<=max;temp++)
  {
      for(j=temp;j>0;j--)
      {
          in[j]=in[j-1];
      }
      in[j]=0;
      inpt = inpt+1;
  }
//  printf("\n***%d\n", inpt);
  stand = in[0];
  k=inpt;
  f=0;
 //for(temp=0;temp<k;temp++)
 //  printf("%d", in[temp]);
  for(temp=1;temp<k;temp++)
  {
   if(in[temp]>0)
   {
       if(stand>=temp)
        stand=stand+in[temp];
       else
       {
           f=f+(temp-stand);
           stand=stand+temp-stand+in[temp];
           //temp=temp-1;
       }
   }
  }
  printf("Case #%d: %d\n", tc, f);
}

return 0;
}

