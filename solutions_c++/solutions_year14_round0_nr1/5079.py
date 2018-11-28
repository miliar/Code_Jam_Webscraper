#include<stdio.h>

int main()
{
   int I,K,L,M,N,Dist[1009],Oil[1009],Tank;
   
   while(scanf("%d %d",&N,&L)==2)
   {
      for(I=0;I<N;I++)
      scanf("%d",&Dist[I+1]);
      for(I=0;I<N;I++)
      scanf("%d",&Oil[I+1]);
      
      long Ans=0;
      Tank=0;
      for(I=0;I<N;I++)
      {
         Tank+=Oil[I+1];
         M=0;
         while(Dist[I+1]>Tank)
         {
            Tank+=Oil[I+1];
            M+=L;
         }
         Ans+=Dist[I+1]+M;
         Tank-=Dist[I+1];
      }
      printf("%d\n",Ans);
   }
   return 0;
}
