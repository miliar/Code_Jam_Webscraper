#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.large.out","w",stdout);
    set<int> digitos;
    int T;
    cin>>T;
    for(int caso=1;caso<=T;caso++){
        long long int N, aux, res;
        cin>>N;
        res=0;
        digitos.clear();
        if(N!=0){
            while(digitos.size()<10){
                 res+=N;
                 aux=res;
                 while(aux>0){
                       digitos.insert(aux%10);
                       aux/=10;
                 }
            }
            cout<<"Case #"<<caso<<": "<<res<<endl;
        } else {
            cout<<"Case #"<<caso<<": INSOMNIA"<<endl;
        }
    }
    return 0;
}
