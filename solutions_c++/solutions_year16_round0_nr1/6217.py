#include<bits/stdc++.h>
using namespace std;
int cn[10];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out4.out","w",stdout);
    int T;
    cin>>T;
    int C=0;
    while(T--){
        long long counter=1;
    C++;
        long long N;
        cin>>N;
        cout<<"Case #"<<C<<": ";
        if(N==0){
            cout<<"INSOMNIA"<<endl;
        }
        else{
        while(true){
            long long x=N*counter;
            while(x>0){
                int dig=x%10;
                cn[dig]=1;
                x/=10;
            }
            counter++;
            long long cner=0;
            for(int i=0;i<=10;i++){
                if(cn[i]==1){
                    cner++;
                }
            }
            if(cner==10){cout<<N*(counter-1)<<endl;break;}
        }
        for(int i=0;i<=10;i++){cn[i]=0;}
        }
    }
return 0;}
