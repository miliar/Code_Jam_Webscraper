#include <bits/stdc++.h>

#define sf scanf
#define pf printf
#define pb push_back
#define PI ( acos(-1.0) )
#define mod 1000000007
#define maxn 100005
#define DBG pf("Hi\n")
#define pb push_back
#define mp make_pair

using namespace std ;

typedef long long int i64 ;

char s[2005] ;
int a[35] ;
int num[15] ;

int main()
{
   int i , j , k , m , n , l , t =1 , tc , x ;

   freopen("inp.in","r",stdin) ;
   freopen("output.txt","w",stdout) ;


   sf("%d",&tc) ;

   while(t<=tc)
   {
      sf("%s",s) ;

      memset(a,0,sizeof(a)) ;
      memset(num,0,sizeof(num)) ;

      for(i=0 ; s[i]!='\0' ; i++ ) a[ s[i]-'A' ]++ ;

      x = a['Z'-'A'] ;
      num[0] += x ;
      a[ 'Z'-'A' ] -= x ;
      a[ 'E'-'A' ] -= x ;
      a[ 'R'-'A' ] -= x ;
      a[ 'O'-'A' ] -= x ;

      x = a['X'-'A'] ;
      num[6] += x ;
      a[ 'S'-'A' ] -= x ;
      a[ 'I'-'A' ] -= x ;
      a[ 'X'-'A' ] -= x ;

      x = a[ 'S' - 'A' ] ;
      num[7] += x ;
      a[ 'S'-'A' ] -= x ;
      a[ 'E'-'A' ] -= x ;
      a[ 'V'-'A' ] -= x ;
      a[ 'E'-'A' ] -= x ;
      a[ 'N'-'A' ] -= x ;

      x = a[ 'G'-'A' ] ;
      num[8] += x ;
      a[ 'E'-'A' ] -= x ;
      a[ 'I'-'A' ] -= x ;
      a[ 'G'-'A' ] -= x ;
      a[ 'H'-'A' ] -= x ;
      a[ 'T'-'A' ] -= x ;

      x = a[ 'W' - 'A' ] ;
      num[2] += x ;
      a[ 'T'-'A' ] -= x ;
      a[ 'W'-'A' ] -= x ;
      a[ 'O'-'A' ] -= x ;

      x = a[ 'T' - 'A' ] ;
      num[3] += x ;
      a[ 'T'-'A' ] -= x ;
      a[ 'H'-'A' ] -= x ;
      a[ 'R'-'A' ] -= x ;
      a[ 'E'-'A' ] -= x ;
      a[ 'E'-'A' ] -= x ;

      x = a[ 'V' - 'A' ] ;
      num[5] += x ;
      a[ 'F'-'A' ] -= x ;
      a[ 'I'-'A' ] -= x ;
      a[ 'V'-'A' ] -= x ;
      a[ 'E'-'A' ] -= x ;

      x = a[ 'F' - 'A' ] ;
      num[4] += x ;
      a[ 'F'-'A' ] -= x ;
      a[ 'O'-'A' ] -= x ;
      a[ 'U'-'A' ] -= x ;
      a[ 'R'-'A' ] -= x ;


      x = a[ 'O' - 'A' ] ;
      num[1] += x ;
      a[ 'O'-'A' ] -= x ;
      a[ 'N'-'A' ] -= x ;
      a[ 'E'-'A' ] -= x ;

      x = a[ 'N'-'A' ]/2 ;
      num[9] += x;
      a[ 'N'-'A' ] -= x ;
      a[ 'I'-'A' ] -= x ;
      a[ 'N'-'A' ] -= x ;
      a[ 'E'-'A' ] -= x ;

      pf("Case #%d: ",t++) ;

      for(i=0 ; i<10 ; i++)
      {
         for( j=1 ; j<=num[i] ; j++ ) pf("%d",i) ;
      }
      pf("\n") ;

   }


   return 0 ;
}
