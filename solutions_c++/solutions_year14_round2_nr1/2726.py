#include<iostream>
#include<string.h>
using namespace std;



int main() {
    freopen( "A-small-attempt1.in", "r", stdin );
    freopen( "A-small-attempt1.out", "w", stdout );
    int t , n , sum=0 ,i=0, j=0 , k=0 ,flag = 0,p , res;
    char c;
    char N[102][102];
    int rep[102]={0};
    int lvar[102] = {0} ;
    cin>>t;
    for(k=1 ; k<=t ; k++ ) {
               cin>>n;
               res = 0;flag=0;
               for( i=0; i<n; i++) { cin>>N[i];   lvar[i] = 0; }
               while( N[0][lvar[0]] != '\0') {
                      sum = 0;
                      c = N[0][lvar[0]];
                      for( i=0; i<n; i++) { rep[i]=0;}
                      for(p=0 ; p<n; p++) {
                              while( N[p][lvar[p]] == c )  { lvar[p]++; rep[p]++;}
                              sum+=rep[p];
                      }
                      for( p=0; p<n; p++) { 
                           if(rep[p] == 0) { flag=1 ;break;}
                      }
                      sum/=n;
                      for( p=0; p<n ; p++ ) {
                             if( sum-rep[p] >0)      res = res +( sum-rep[p] );
                             else                  res+=(rep[p]-sum);
                           }
               }
               for( i=0; i<n; i++) {
                         if( lvar[i] != strlen(N[i]) ) { flag=1; break;}
                    }
               if(flag==0) 
               cout<<"Case #"<<k<<": "<<res<<endl;
               else
               cout<<"Case #"<<k<<": Fegla Won"<<endl;
    }
               
               
    return 0;
}
