#include<stdio.h>
int a[20],r;

void cue( long long int n ){
  while( n > 0 ){
     if( a[ n%10 ] == 0 ){
       a[n%10]++;
       r--;
     }
     n /= 10LL;
  }

}

int main(){
   int i,t, c, m;
   long long int n;
      scanf("%d",&t);
      for( c = 1 ; c <= t ; c++ ){
         scanf("%lld",&n);
         if( n != 0 ) {
            r = 10;
            a[0] = a[1] = a[2] = a[3] = a[4] = a[5] = a[6] = a[7] = a[8] = a[9] = 0;
            m = 0;
            while( r != 0 ){
               m++;
               cue( n* (long long int)m );
            }
            printf("Case #%d: %lld\n",c,n*(long long int)m);
         }
         else
            printf("Case #%d: INSOMNIA\n",c);
      }
   return 0;
}
