#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std ;

int t , x , y , u=0 ;

int main()  
{   
   scanf("%d",&t) ; 
   while(t--)
   {
      scanf("%d",&x) ; int f[17]={0} ;
      for(int i=1 ; i<=4 ; i++) for(int j=1 ; j<=4 && scanf("%d",&y) ; j++) if(i==x) f[y]++ ;

      scanf("%d",&x) ;
      for(int i=1 ; i<=4 ; i++) for(int j=1 ; j<=4 && scanf("%d",&y) ; j++) if(i==x) f[y]++ ;

      int ans=0; 
      for(int i=1 ; i<=16 ; i++) if(f[i]>1) ans=(!ans)?i:17 ;

      printf("Case #%d: ",++u) ;
      if(ans && ans<=16)  printf("%d\n",ans) ;
      else printf(!ans ?"Volunteer cheated!\n":"Bad magician!\n") ; 
   } 
   
 return 0 ;
}