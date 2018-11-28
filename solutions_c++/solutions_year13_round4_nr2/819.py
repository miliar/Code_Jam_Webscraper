#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<set>
#include<vector>
#include<map>

using namespace std;

#define For(Q,W) for(int Q=0;Q<W;Q++)
#define ForL(Q,W) for(long long Q=0;Q<W;Q++)

#define LLD long long
#define mkp make_pair
#define pf printf
#define sf scanf

//#define debug
#ifdef debug
#define db(XZ) cout<<XZ<<" "
#define dbn() cout<<endl
#else 
#define db(XZ); 
#define dbn()
#endif

LLD lastone(LLD x){ return x&(x^(x-1)); }

void solve(int kolko){
     LLD N, P;
     cin>>N>>P;
     LLD vys1=0;        
     LLD vys2=0;
     
     if(P== 1<<N){ vys1=vys2=P-1;
     }
     else{
          LLD jed=1;
          LLD npom=N;
          while(P>= 1<<jed){
                     vys2= vys2*2+1;
                     npom--;   
                     jed++;          
          }
          vys2= vys2<<npom;
          LLD mask=(1<<(N-1));
          jed=0;
          db((mask&(P-1)));
          while( (((P-1)& mask) == mask) && mask>=1){ jed++; mask=mask/2;}
          
          db(P-1);db(jed);
          vys1= (1<<(jed+1))-2;
               
     }
     cout<<"Case #"<<kolko<<": ";
     cout<<vys1<<" "<<vys2;
     cout<<endl;
     
}

int T;

int main(){
    cin>>T;
    For(t,T){
         solve(t+1);    
    }
    return 0;   
}
