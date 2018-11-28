#include <bits/stdc++.h>
 
using namespace std;
#define sd(t) scanf("%d" , &t)  
#define sdl(t) scanf("%lld" , &t)  
#define sdd(t) scanf ("%lf" , &t)
#define  ll long long 
 #define f(i , a , n)  for ( i=a ; i<=n ; i++ )
 #define fr( i , a , n ) for ( i=a ; i>=n ; i-- )
#define mp make_pair
#define pb push_back
#define F first = 0 ; 
#define S second
#define maxn 505
#define maxr 1005
#define MODA  1000000007
#define INF  1000000000000000000ll
 


int main()

{
  int t  ;  sd(t) ; 
int T = t ; 

  while (t--)
{ string s ; 
	cin>>s ; 

 int l = s.length() ;
int x=-1 ; 
int i ; f ( i ,0 , l-1) { if(s[i]=='-') x= i ;  }

if(x==-1)  { printf("Case #%d: 0\n" ,T-t ) ;  continue ; } 
int ans = 1 ; bool y = true ;  
fr ( i , x-1 , 0 ) { if(s[i]=='+' && y == true  ) {ans++ ; y = false ;  } if(s[i]=='-' && y == false ) {ans++ ; y = true ;  }   }

printf("Case #%d: %d\n" ,T-t ,  ans) ; 
 
}
}