#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std ;

int t , n , u=0 ;
double a[1001] , b[1001] ;

int main()  
{   
   scanf("%d",&t) ; 
   while(t--)
   {
      scanf("%d",&n) ;
      for(int i=0 ; i<n ; i++)  scanf("%lf",&a[i]) ;
      for(int i=0 ; i<n ; i++)  scanf("%lf",&b[i]) ; 
      sort(a,a+n) ; sort(b,b+n) ;
      
      //for(int i=0 ; i<n ; i++) printf("%lf ",a[i]) ; puts("") ;
      //for(int i=0 ; i<n ; i++) printf("%lf ",b[i]) ; puts("") ;
      
      int j=0 , k=n-1 , l=n-1 , x=0 ; 
      while(j<n)
      {
          while(k>=0 && l>=0 && a[l]>b[k]) x++ , k-- , l-- ; 
          if(k<0 || l<0 || j>l) break ;
          j++ ; k-- ;  
      }
      
      j=0 , k=0 ; 
      while(j<n)
      {
          while(k<n && a[j]>b[k]) k++ ;
          if(k>=n) break ;
          j++ ;  k++ ; 
      }
      
      printf("Case #%d: %d %d\n",++u,x,n-j) ; 
   } 
   
 return 0 ;
}