#include <bits/stdc++.h>

using namespace std;

void solvre(long long x){
    bool flag[10] = {false};
    int cont = 0;
    long long ans = 0;
    long long aux;

    while(cont<10){
        ans++;
        aux = x*ans;
        while(aux>0){
            if(!flag[aux%10]){
                flag[aux%10] = true;
                cont++;
            }
            aux/=10;
        }
    }
    cout<<ans*x<<endl;
}

int main(){
    int x;
    int n;

    cin>>n;
    for(int i = 1; i<=n; i++){
        cin>>x;
        cout<<"Case #"<<i<<": ";
        if(x==0) cout<<"INSOMNIA\n";
        else solvre(x);
    }


}
