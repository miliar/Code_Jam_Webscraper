#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int t, restantes;
    long long n, aux;
    bool numbers[11];
    cin>>t;
    for(int i = 0; i < t; i++){
        cout<<"Case #"<<i+1<<": ";
        cin>>n;
        if(!n){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        for(int j = 0; j < 11; j++){
            numbers[j] = false;
            restantes = 10;
        }
        long long k;
        for(k = 1; restantes ; k++){
            aux = k * n;
            while(aux){
                if(!numbers[aux % 10]){
                    numbers[aux % 10] = true;
                    restantes--;
                }
                aux /= 10;
            }

        }
        cout<<n * (k - 1)<<endl;
    }
    return 0;
}
