#include<stdio.h>
#include<string.h>

int main()
{
   int T, t, i, j;
   int q, card[2][4], tmp[4], c;

   scanf("%d",&T);
   while( t++ < T )
   {
      scanf("%d",&q);
      for( i=0; i<4 ; i++ )
      {  scanf("%d %d %d %d",tmp,tmp+1,tmp+2,tmp+3);
         if( i+1 == q )   memcpy(card[0], tmp, sizeof(int)*4);
      }
      scanf("%d",&q);
      for( i=0; i<4 ; i++ )
      {  scanf("%d %d %d %d",tmp,tmp+1,tmp+2,tmp+3);
         if( i+1 == q )   memcpy(card[1], tmp, sizeof(int)*4);
      }

      c = 0;
      for( i=0; i<4 ; i++ )
      {
         if( c == -1 )   break;
         for( j=0; j<4 ; j++ )
             if( card[0][i] == card[1][j] )
             {   if(  c != 0 )
                 {  c = -1;
                    break;
                 }
                 c = card[0][i];
                 break;
             }
       }
       
       printf("Case #%d: ", t);
       if( c == -1 )    printf("Bad magician!\n");
       else if( c == 0 )    printf("Volunteer cheated!\n");
       else   printf("%d\n",c);
   }  
   return 0;
}
