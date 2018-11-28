#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <cmath>
using namespace std;
bool pal(int x );
int main()
{
     freopen("input.txt","r",stdin) ;
     freopen("output.txt","w",stdout) ;
     int a , b , t  , c , y;
     cin>>t ;
     for(int j = 0 ; j<t ; j++){
          cin>>a>>b ;
         c = a ;
        y = b ;
        a = min(c, y) ;
        b = max(c, y) ;
         c = 0 ;
     for(int i = a ;i <=b ;i++ ){
             y =   sqrt(i) ;
          if(y*y==i&&pal(i)&&pal(y))c++ ;
     }
     cout<<"Case #"<<j+1<<": "<<c<<endl ;
     }
    return 0;
}
bool pal(int x ){
     if(x<10)return true ;
     string s ;
     stringstream conv ;
     conv<<x ;
     s=conv.str() ;

     for(int i = 0 ; i<s.size()/2 ; i++){
          if(s[i]!=s[s.size()-1-i])return false ;
     }
     return true;
}
