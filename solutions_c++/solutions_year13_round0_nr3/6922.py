#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;
int m[1020],t,p;
char c[30];
int pali( int n ){
  int l,i,b;
  char a[30];
    sprintf( a , "%d" , n );
    sprintf( c , "%d" , n );
    l = strlen( a );
    reverse( c + 0 , c + l );
    b = strcmp( a , c );
  return b;
}
void insert( int n ){
  int i;
    m[ n ] = m[ p ] + 1 ;
    for( i = p+1 ; i < n ; i++ )
      m[i] = m[p];
    p = n;
}
int main(){
  int i,j,l,a,b;
    p = 1; m[1]=1;
    for( i = 2 ; i <= 35 ; i++ ){
       if( pali(i) == 0 && pali(i*i) == 0  )
        insert( i * i  );
    }
    insert( 1000 );  m[ 1000 ]--;
    scanf("%d",&t);
    j = 1 ;
    while( j <= t ) {
      scanf("%d%d",&a,&b);
      printf("Case #%d: %d\n",j, m[ b ] - m[ a - 1 ]);
      j++;
    }
  return 0;
}
