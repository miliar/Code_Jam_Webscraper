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
{ map < int , int > m ; 
 int n , i   ; sd(n) ; 

  f ( i  ,1, 100)
 {
    int a = n* i ; int b = a ;  

    while (a!=0) { int x = a%10 ; a/=10 ; m[x]=1 ;    }
 int j ; 
    f ( j, 0 , 9 )
  {
     if(m[j]!=1) break ; 

  }

if(j==10) {  printf("Case #%d: %d\n" ,T-t ,  b  ) ; break ; } 


 }


if(i==101) printf("Case #%d: INSOMNIA\n" , T-t ) ; 
 
}







}