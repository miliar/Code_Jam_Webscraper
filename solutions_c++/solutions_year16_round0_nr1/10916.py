#include <bits/stdc++.h>
using namespace std;
int main()
{long long n , i , j, k , tc  ;
ifstream in ("A-large.in") ;
ofstream op ("output.in") ;
in>>tc ;
for(k=1 ;k<=tc ; k++){ j=1 ;
in>>n  ;
if(n==0){op<<"Case #"<<k<<": INSOMNIA"<<endl ; continue ;}
set <int> y;
bool c=false ;
while(j>0){
     string x ;
     stringstream sso;
     sso<<n*j ;
     sso>>x ;
     for(i=0; i<x.size() ; i++){y.insert(x[i]);
                    if(y.size()==10){op<<"Case #"<<k<<": "<<n*j<<endl;
                                         c=true ;   break ;  }}
    if(c){break;}  j++ ;
         }
}


return 0 ;}

