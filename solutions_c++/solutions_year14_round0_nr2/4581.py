#include<stdio.h>
#include<fstream>
#include<iomanip>
#include<cstring>
#include<algorithm>
using namespace std ;

int t , u=0 ;
double c , f , x ;

int main()  
{   
   ifstream in("s.txt") ; FILE* out=fopen("a.txt","w") ;  
   in >> t ;
 
   while(t--)
   {
      
      in >> c >> f >> x  ;
      if(c>x) { fprintf(out,"Case #%d: %.7lf\n",++u,(x/2.0)) ; continue ; } 

      double cur=2.0 , t=0.0 ;
      while( ((x-c)/cur) > (x/(cur+f)) ) { t+=(c/cur) ; cur+=f ; }
      t+=x/cur ;
      
      fprintf(out,"Case #%d: %.7lf\n",++u,t) ;
   } 
   in.close() ; fclose(out) ;
   
 return 0 ;
}
