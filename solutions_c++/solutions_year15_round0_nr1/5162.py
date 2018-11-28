#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;

char personas[1002];

int T;
int N;
int res;
int suma;

int main(){
    optimizar_io(0);
    cin>>T;
    for(int caso=1;caso<=T;caso++){
        cin>>N;
        for(int i=0;i<=N;i++)
            cin>>personas[i];
        suma=res=0;
        for(int i=0;i<=N;i++)
            if(suma<i){
                res+=i-suma;
                suma=i+personas[i]-'0';
            } else {
                suma+=personas[i]-'0';
            }
        cout<<"Case #"<<caso<<": "<<res<<"\n";
    }
    return 0;
}
