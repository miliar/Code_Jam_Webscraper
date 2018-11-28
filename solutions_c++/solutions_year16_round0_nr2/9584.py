#include<stdio.h>
#include<string.h>
int main(){
char a[200];
   int t,n,i,c,b,r;
      scanf("%d",&n);
      for( c = 1 ; c <= n; c++ ){
         scanf(" %s",a);
         t = strlen(a);
         if( a[0] == '-' )
           b = 1;
         else
           b = 0;
         for( i = 0 , r = 0 ; i < t-1 ; i++ )
           if( a[i] == '+' && a[i+1] == '-' )
             r++;
         printf("Case #%d: %d\n",c,(r*2)+b);
      }
   return 0;
}
