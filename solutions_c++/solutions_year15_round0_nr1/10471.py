#include <stdio.h>

int main(int argc, char *argv[])
{
    int maxshy,T,S[1000],shy,counter,friends[101]={0},k;
    scanf("%d",&T);

   for(int i=1;i<=T;i++)
   {

    scanf("%d",&maxshy);
    scanf("%d",&shy);

    for(int j=maxshy;j>=0;j--)
    {
        S[j]= shy%10;
        shy=shy/10;
    }

     counter=0;
     for(k=0;k<=maxshy;)
     {
         if(counter >= k)
            {counter += S[k];k++;}
          else{
            friends[i]++;
            counter++;
          }
     }

   }
   for(int i=1;i<=T;i++)
    printf("Case #%d: %d\n",i,friends[i]);
   return 0;
}
