#include <iostream>
#include <cstring>

using namespace std;

int main()
{
   int T,A,B,Match,NumMatch;
   bool N[17];
   scanf("%d",&T);
   for ( int w = 1; w <= T; w++) {
       memset(N,false,sizeof(N));
       Match = 0;
       scanf("%d",&A);
       A--;
       for ( int i = 0; i < 4; i++){
           for ( int j = 0; j < 4; j++) {
               scanf("%d",&B);
               if ( i == A ) N[B] = true; 
           }
       }
       
       scanf("%d",&A);
       A--;
       for ( int i = 0; i < 4; i++){
           for ( int j = 0; j < 4; j++) {
               scanf("%d",&B);
               if ( i == A ) {
                   if ( N[B] == true) {
                       Match++;
                       NumMatch = B;
                   } 
               }
           }
       }
       
       if ( Match == 1 ) {
           printf("Case #%d: %d\n",w,NumMatch);
       } else if ( Match > 1 ) {
           printf("Case #%d: Bad magician!\n",w);
       } else {
           printf("Case #%d: Volunteer cheated!\n",w);
       }
   }
   
   return 0;
}
