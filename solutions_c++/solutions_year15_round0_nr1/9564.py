#include<cstdio>
int t,n,a;
char b[1020];
using namespace std;
int main(){
  int i,j,p,c;
     scanf("%d",&t);
     j = 1;
      while( t-- ){
        scanf("%d %s",&n,b);

        for( i = 0 , p = 0 , c = 0 ; i <= n ; i++ ){
           a = b[i]-'0';
           if( p >= i )
             p += a;
           else{
             c +=  i - p ;
             p += ( i - p ) + a ;
           }
        }

        printf("Case #%d: %d\n",j++,c);
     }
  return 0;
}
