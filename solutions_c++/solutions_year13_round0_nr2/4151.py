#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
int x[101][101] ;
int y[101] ;
int z[101] ;
int main()
{
      freopen("input.txt","r",stdin) ;
     freopen("output.txt","w",stdout) ;
     int t  , c , h ;
     int m , n , mx , mn  ;
     bool f , yes = false   ;
     cin>>t ;
     for(int i = 0 ; i<t ; i++){
          cin>>n>>m ;
          memset(y , -1 , sizeof(y)) ;
          memset(z , -1 , sizeof(z)) ;
           yes = false ;

          for(int k = 0 ; k<n ; k++){
               for(int j = 0 ; j<m  ; j++){
                    cin>>x[k][j] ;
               }
          }
          for(int  k = 0 ; k<n ; k++){
                  //  f = false ;
                   // h = x[k][0] ;
                    mx = -1 ;
               for(int j = 0 ; j <m ; j++){
                    mx = max(mx , x[k][j]) ;
               }
               z[k] = mx ;

          }
          for(int k = 0 ; k<m ; k++){
               //f= false ;
               //h = x[0][k] ;
               mx =-1 ;
               for(int j = 0 ; j<n ; j++){
                    mx = max(mx, x[j][k]) ;
               }
              y[k] = mx ;
          }
          for(int k = 0 ; k<n ; k++){
               for(int j = 0 ; j<m ; j++){
                    if(min(z[k], y[j])!=x[k][j]){
                         yes = true ;
                         cout<<"Case #"<<i+1<<": NO"<<endl ;
                         break ;
                    }
               }
               if(yes)break ;
          }
         if(!yes)  cout<<"Case #"<<i+1<<": YES"<<endl ;
     }

    return 0;
}
