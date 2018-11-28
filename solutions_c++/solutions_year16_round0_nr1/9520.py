#include<bits/stdc++.h>
using namespace std;
const long long GG = (1LL<<(10))-1LL;
int main(){
    int T;
    long long N,R,J,F;
    string L;
    cin>>T;
    for(int t = 1; t <= T; t++){
       cin>>N;
       bool FLAG = 0;
           R = 0LL;
           J = 2LL;
           F = N;
           int H = 100000;
           while(H--){
                L = to_string(F);
                for(int i = 0; i < L.size(); i++){
                     int h = L[i] - '0';
                     R = R|(1LL<<h);                      
                }
                if(R == GG){
                    cout<<"Case #"<<t<<": "<<L<<endl;
                    FLAG = 1;
                    break;            
                }else{
                    F =J*N;
                    J++;
                }
           }
           if(!FLAG)cout<<"Case #"<<t<<": INSOMNIA"<<endl;
    }
}