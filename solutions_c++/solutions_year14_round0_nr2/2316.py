#include<iostream>
#include<cstdio>
#include<cstring>
#include<iomanip>

using namespace std;

double C,F,X;
double best;

int main(){
    int T; cin>>T;
    
    for(int t=1;t<=T;t++){
            cin>>C>>F>>X;
            
            best = X / 2;
            
            int farms = 1;
            while( 1 ){
                   
                   double temp = 0, start = 2;
                   for(int i=1;i<=farms;i++){
                           temp += C / start;
                           start += F;
                           }
                   temp += X / start;
                   
                   if( temp < best )
                       best = temp;
                   else
                       break;
                   
                   farms++;
                   }
            cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<best<<'\n';
            }
    
    return 0;
}
